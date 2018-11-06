#! /usr/bin/python3

import os
import re
import random

patterns = ['bicycle', 'fish', 'rocket', 'tree', 'walking']#, 'cat', 'seedling', 'trophy' , 'crow', 'truck']

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


# Compute the data content
# TODO: here, we may skew the random generation, or trick it another way
data = [[0 for j in range(cardsize * ycard)] for i in range(cardsize * xcard)]
for x in range(cardsize * xcard):
    for y in range(cardsize * ycard):
        data[x][y] = int(random.uniform(0,len(patterns)))
    
# Helping function
def cell_to_viewport(pattern, x, y):
    vx=pmargin + x*cellsize + (0.5+int(x/(cardsize)))*cmargin + xpad[pattern]
    vy=pmargin + y*cellsize + (0.5+int(y/(cardsize)))*cmargin + ypad[pattern]
    return 'x="{:f}" y="{:f}"'.format(vx, vy)

## Generate the file 
f = open("board.svg", "w")
f.write('<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"\n')
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
