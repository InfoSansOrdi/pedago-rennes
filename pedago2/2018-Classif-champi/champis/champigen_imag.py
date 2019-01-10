#! /usr/bin/python3

import os
import re
import random

skew=True # Skew the pattern generation to get more of the first pattern
letter=False # Print on letter paper (or on A4 if false)

files_feet = { 'double': ['foot_double',
			  'shadow_double_bot',
			  'shadow_double_top',
			  ],
	       'inverted': ['foot_inverted',
			    'shadow_inverted',
			    ],
	       'without': ['foot_without']
	}

files_hat = {'flat': ['hat_flat_bot',
		      'hat_flat_top',
		      'dots_flat',
		      ],
	     'convex': ['hat_convex',
			'dots_convex',
			],
	     'bell': ['hat_bell',
		      'dots_bell',
		      ],
	     'conical': ['hat_conical',
			 'dots_conical',
			 ]
	     }

files_icons = ['cow', 'snail', 'bird', 'death']

hats = {} #hats[hatname]
dots = {} #dots[hatname]
feet = {} #feet[footname]
icons = {} #icons[iconname]

file_shadow_hat = 'shadow_hat'

colors = ['green', 'blue', 'red']

nb_colors = len(colors)

pmargin=0 # page margin, in the unit of the viewBox
cmargin=0 # margin within the card
cellsize=2100 # cell of one icon, in the unit of the viewBox

cardsize=1 # Each card has cardsize x cardsize icons
xcard=6 # There is xcard x ycard on a given page
ycard=8 #


## compute some globals
grad = {} # <linearGradient></linearGradient> data
paths = {} # <path> data drawing the pattern
# Each image is meant to be printed on a viewBoxes of a specific size: 512x512, 640x512 or 320x512 (check their svg header)
# so we need to compute extra padding to center them in the cell: xpad and ypad
xpad = {}
ypad = {}
random.seed(None)

## Read the image files and prepare the data

#regex to parse the svg
repath = re.compile("<path[^>]*/>")
rebox = re.compile('viewBox="0 0 ([^ ]*) ([^"]*)"')
restyle = re.compile('"/>')
reid = re.compile('id="[a-zA-Z0-9_-]*"')

regrad = re.compile("<linearGradient[^^]*linearGradient>")

for filename in files_icons:
	svgfile = open("svg_parts/{:s}.svg".format(filename), "r")
	svgstr = svgfile.read()

	path = repath.search(svgstr).group()

	icons[filename] = restyle.sub('" fill-rule="evenodd"/>'.format(filename), path)

	print('{:s}: {:s}\n'.format(filename, icons[filename]))


for hatname, filenames in files_hat.items():
	hats[hatname] = ""
	for filename in filenames:
		svgfile = open("svg_parts/{:s}.svg".format(filename), "r")
		svgstr = svgfile.read()

		path = repath.search(svgstr).group()
		if 'shadow' in filename:
			grad = regrad.search(svgstr).group()
			grad = reid.sub('id="{:s}"'.format(filename), grad)
			path = restyle.sub('" fill="url(#{:s})"/>'.format(filename), path)
			hats[hatname] += ('\n{:s}\n{:s}'.format(grad, path))
		elif 'dots' in filename:
			dots['dot_'+hatname] = path
		elif 'flat_bot' in filename:
			hats[hatname] += restyle.sub('" filter="url(#brightness)"/>', path)
		else:
			hats[hatname] += path

	print('{:s}: {:s}\n'.format(hatname, hats[hatname]))


for footname, filenames in files_feet.items():
	feet[footname] = ""
	for filename in filenames:
		svgfile = open("svg_parts/{:s}.svg".format(filename), "r")
		svgstr = svgfile.read()

		path = repath.search(svgstr).group()
		if 'shadow' in filename:
			grad = regrad.search(svgstr).group()
			grad = reid.sub('id="{:s}"'.format(filename), grad)
			path = restyle.sub('" fill="url(#{:s})"/>'.format(filename), path)
			feet[footname] += ('\n{:s}\n{:s}'.format(grad, path))
		else:
			feet[footname] += path

	# shadow from hat
	svgfile = open("svg_parts/{:s}.svg".format(file_shadow_hat), "r")
	svgstr = svgfile.read()
	path = repath.search(svgstr).group()
	grad = regrad.search(svgstr).group()
	grad = reid.sub('id="{:s}"'.format(file_shadow_hat), grad)
	path = restyle.sub('" fill="url(#{:s})"/>'.format(file_shadow_hat), path)
	feet[footname] += ('\n{:s}\n{:s}'.format(grad, path))

	print('{:s}: {:s}\n'.format(footname, feet[footname]))

nb_hats = len(list(hats))
nb_feet = len(list(feet))
nb_elements = 10

# Compute the data content
data = [[-1 for j in range(cardsize * ycard)] for i in range(cardsize * xcard)]
for xc in range(xcard):
	for yc in range(ycard):
		curamounts = [0 for i in range(nb_elements)]
		for x in range(cardsize):
			for y in range(cardsize):
				if skew:
					p = int(random.uniform(0,nb_elements+2))
					if p > (nb_elements-1):
						p=0
				else:
					p = int(random.uniform(0,nb_elements))
				curamounts[p] += 1
				data[x+xc*cardsize][y+yc*cardsize] = p
		print(curamounts, sum(curamounts))

# Helping function
def cell_to_viewport(x, y):
	vx=pmargin + x*cellsize + (0.5+int(x/(cardsize)))*cmargin #+ xpad[pattern]
	vy=pmargin + y*cellsize + (0.5+int(y/(cardsize)))*cmargin #+ ypad[pattern]
	return 'x="{:f}" y="{:f}"'.format(vx, vy)


def loved_by_cow(color, hat, foot, dot):
	if foot == 'inverted':
		return color != 'blue'
	elif foot == 'double':
		return hat == 'bell' or hat == 'conical'
	elif foot == 'without':
		return 'dot' not in dot

def death_for_humans(color, hat, foot, dot):
	if color == 'green':
		return 'dot' in dot

	elif color == 'red':
		if hat == 'bell':
			return True
		elif hat == 'convex':
			return False
		elif hat == 'conical' and 'dot' in dot:
			return True
		elif hat == 'flat' and 'dot' not in dot:
			return True
		else:
			return False

	elif color == 'blue':
		return foot != 'double'

def loved_by_bird(color, hat, foot, dot):
	if hat == 'bell':
		return foot != 'double'

	elif hat == 'convex':
		return color == 'green'

	elif hat == 'conical':
		return foot != 'without'

	elif hat == 'flat':
		return color != 'blue'

def loved_by_snail(color, hat, foot, dot):
	if color == 'green':
		return True

	elif color == 'blue' and 'dot' not in dot:
		return True

	else:
		return False


## Generate the file
f = open("board.svg", "w")
f.write('<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"\n')

if letter:
	f.write(' viewBox="0 0 14000 19800" height="11in" width="8.5in">\n') # 14000x19800 is 21000x29700 at 2/3 ratio
else:
	f.write(' viewBox="0 0 21000 29700" height="297mm" width="210mm">\n') # 14000x19800 is 21000x29700 at 2/3 ratio
#	f.write(' viewBox="0 0 14000 19800" height="594mm" width="420mm">\n') # 14000x19800 is 21000x29700 at 2/3 ratio

f.write('<style>\n')

for color in colors:
	f.write('.{:s}Fill {{\n'.format(color))
	f.write('\tfill: {:s};\n'.format(color))
	f.write('}\n')

f.write('</style>\n')

f.write('<defs>\n')

#darker part of the flat hat
darken_filter = '''
<filter id="brightness">
  <feComponentTransfer>
    <feFuncR type="linear" slope="0.6"/>
    <feFuncG type="linear" slope="0.6"/>
    <feFuncB type="linear" slope="0.6"/>
  </feComponentTransfer>
</filter>
'''

f.write(darken_filter)

for footname, foot_def in feet.items():
	f.write('<g id="{:s}">\n{:s}\n</g>\n'.format(footname, foot_def))

for hatname, hat_def in hats.items():
	f.write('<g id="{:s}">\n{:s}\n</g>\n'.format(hatname, hat_def))

for dotname, dot_def in dots.items():
	f.write('<g id="{:s}">\n{:s}\n</g>\n'.format(dotname, dot_def))

for iconname, icon_def in icons.items():
	f.write('<g id="{:s}">\n{:s}\n</g>\n'.format(iconname, icon_def))

#for pat in patterns:
#	f.write('  <g id="{:s}">{:s}</g>\n'.format(pat, paths[pat]))
f.write('</defs>\n')

# Cells content
for x in range(cardsize * xcard):
	for y in range(cardsize * ycard):

		idx_hat = random.randint(0, nb_hats-1)
		hat = list(hats)[idx_hat]

		idx_feet = random.randint(0, nb_feet-1)
		foot = list(feet)[idx_feet]

		color_idx = random.randint(0, nb_colors-1)
		color = colors[color_idx]

		f.write('<use class="{:s}Fill" xlink:href="#{:s}" {:s} />\n'.format(color, foot, cell_to_viewport(x,y)))
		f.write('<use class="{:s}Fill" xlink:href="#{:s}" {:s} />\n'.format(color, hat, cell_to_viewport(x,y)))

		p_threshold = 0.5
		p = random.uniform(0,1)
		dot = ""
		if p > 1-p_threshold:
			dot = 'dot_'+hat
			f.write('<use fill="maroon" xlink:href="#{:s}" {:s} />\n'.format(dot, cell_to_viewport(x,y)))

		if loved_by_cow(color, hat, foot, dot):
			f.write('<use xlink:href="#cow" {:s} />\n'.format(cell_to_viewport(x,y)))
		if loved_by_snail(color, hat, foot, dot):
			f.write('<use xlink:href="#snail" {:s} />\n'.format(cell_to_viewport(x,y)))
		if loved_by_bird(color, hat, foot, dot):
			f.write('<use xlink:href="#bird" {:s} />\n'.format(cell_to_viewport(x,y)))
		if death_for_humans(color, hat, foot, dot):
			f.write('<use xlink:href="#death" {:s} />\n'.format(cell_to_viewport(x,y)))


# Grid to help cutting the cards
for x in range(xcard):
	for y in range(ycard):
		f.write('<rect x="{:f}" y="{:f}" width="{:f}" height="{:f}" {:s} />'
		.format(pmargin+x*cellsize*(cardsize), pmargin+y*cellsize*(cardsize), cellsize*(cardsize), cellsize*(cardsize),
		'style="stroke:#c4c4c4;stroke-width:3;stroke-opacity:1;fill:none"'))
f.write('</svg>\n')
f.close()

os.system("inkscape --export-pdf=board.pdf board.svg")
#os.unlink("board.svg")
