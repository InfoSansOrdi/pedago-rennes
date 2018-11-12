#! /usr/bin/python3

import os
import re
import random

skew=False # Skew the pattern generation to get more of the first pattern
crc=False # Generate only cards where the amount of each card is s.t. X%3 = 1
letter=True # Print on letter paper (or on A4 if false)

patterns = ['bicycle',  'rocket', 'tree', 'walking']#'fish',, 'cat', 'seedling', 'trophy' , 'crow', 'truck']

pmargin=1200 # page margin, in the unit of the viewBox
cmargin=645 # margin within the card
cellsize=645 # cell of one icon, in the unit of the viewBox

cardsize=5 # Each card has cardsize x cardsize icons
xcard=3 # There is xcard x ycard on a given page
ycard=4 #


## compute some globals
paths = {} # <path> data drawing the pattern
# Each image is meant to be printed on a viewBoxes of a specific size: 512x512, 640x512 or 320x512 (check their svg header)
# so we need to compute extra padding to center them in the cell: xpad and ypad
xpad = {}
ypad = {}
random.seed(None)

## Read the image files and prepare the data
repath = re.compile("<path[^>]*>")
rebox = re.compile('viewBox="0 0 ([^ ]*) ([^"]*)"')
for filename in patterns:
    svgfile = open("img/{:s}.svg".format(filename), "r")
    svgstr = svgfile.read()
    paths[filename] = repath.search(svgstr).group()
    box = rebox.search(svgstr)
    
    xpad[filename] = (cellsize - int(box.group(1))) / 2
    assert xpad[filename] > 0, "the cell is too small for {:s}.svg: cellsize is {:d} but image is x{:s} y{:s}".format(filename, cellsize, box.group(1), box.group(2))
    
    ypad[filename] = (cellsize - int(box.group(2))) / 2
    assert ypad[filename] > 0, "the cell is too small for {:s}.svg: cellsize is {:d} but image is x{:s} y{:s}".format(filename, cellsize, box.group(1), box.group(2))


# Generate a distribution of icons, skewed or not
# The number of each pattern in one batch will always be so that XX % 3 == 1
def generate_amounts(target_size):
    assert (target_size - len(patterns)) % 3 == 0, "the batch size {:d} modulo 3 is not 1".format(target_size)
    total = int((target_size - len(patterns)) / 3)
    amounts_res = [0 for i in range(len(patterns))]
    if skew:
        for i in range(total):
            x = random.randint(0, len(patterns)+1)
            if x>len(patterns)-1: # There will be some more pattern=0
                x=0
            amounts_res[x] += 1
#        cursum = 0
#        for i in range(len(amounts_res) - 1):
#            x = random.randint(0, total - cursum - (len(amounts_res) - i))
#            cursum += x
#            amounts_res[i] = x
#            amounts_res[-1] = total - cursum
    else:
        for i in range(total):
            x = random.randint(0, len(patterns)-1)
            amounts_res[x] += 1
    amounts_res = [3 * e +1 for e in amounts_res]
    assert sum(amounts_res) == target_size, "This should not happen: {:d} != {:d}".format(sum(amounts_res), target_size)
    return amounts_res

# Compute the data content
# Generation is done using the distribution computed above
data = [[-1 for j in range(cardsize * ycard)] for i in range(cardsize * xcard)]
for xc in range(xcard):
    for yc in range(ycard):
        amounts = generate_amounts(cardsize * cardsize)
        pool = [i for i in range(len(patterns))]
        curamounts = [0 for i in range(len(amounts))]
        for x in range(cardsize):
            for y in range(cardsize):
                if crc:
                    p = random.choice(pool)
                    curamounts[p] += 1
                    if curamounts[p] >= amounts[p]:
                        del pool[pool.index(p)]
                else:
                    p = int(random.uniform(0,len(patterns)))
                    curamounts[p] += 1
                data[x+xc*cardsize][y+yc*cardsize] = p
        print(curamounts, sum(curamounts))
    
# Helping function
def cell_to_viewport(pattern, x, y):
    vx=pmargin + x*cellsize + (0.5+int(x/(cardsize)))*cmargin + xpad[pattern]
    vy=pmargin + y*cellsize + (0.5+int(y/(cardsize)))*cmargin + ypad[pattern]
    return 'x="{:f}" y="{:f}"'.format(vx, vy)

## Generate the file 
f = open("board.svg", "w")
f.write('<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"\n')
if letter:
    f.write('     viewBox="0 0 14000 19800" height="11in" width="8.5in">\n') # 14000x19800 is 21000x29700 at 2/3 ratio
else:
    f.write('     viewBox="0 0 14000 19800" height="297mm" width="210mm">\n') # 14000x19800 is 21000x29700 at 2/3 ratio
f.write('<defs>\n')
for pat in patterns:
    f.write('  <g id="{:s}">{:s}</g>\n'.format(pat, paths[pat]))
f.write('</defs>\n')

# Cells content
for x in range(cardsize * xcard):
    for y in range(cardsize * ycard):
        pat = patterns[ data[x][y] ]
        f.write('<use xlink:href="#{:s}" {:s} />\n'.format(pat, cell_to_viewport(pat, x,y)))
# Grid to help cutting the cards
for x in range(xcard):
    for y in range(ycard):
        f.write('<rect x="{:f}" y="{:f}" width="{:f}" height="{:f}" {:s} />'
                .format(pmargin+x*cellsize*(cardsize+1), pmargin+y*cellsize*(cardsize+1), cellsize*(cardsize+1), cellsize*(cardsize+1),
                        'style="stroke:#c4c4c4;stroke-width:3;stroke-opacity:1;fill:none"'))
f.write('</svg>\n')
f.close()

os.system("inkscape --export-pdf=board.pdf board.svg")
os.unlink("board.svg")
