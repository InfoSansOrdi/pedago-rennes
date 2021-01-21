#! /usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "Kerian Thuillier"
__email__ = "kerian.thuillier@ens-rennes.fr"

#IMPORT#########################################################################
import os
import math
import shutil
import argparse
import subprocess

#PARAMETERS#####################################################################

#GLOBAL#VARIABLES###############################################################

###
# TEMPORARY FILES PATHS
Current_path = os.path.dirname(os.path.realpath(__file__))
SVG_path = Current_path + '/.temp/svg/'
PDF_path = Current_path + '/.temp/pdf/'

###
# DATAS
A4 = (210, 297)
A4_margin = (20, 33)

###
# DRAWING PARAMETERS
Identifiant = 0.65
Indication = (0.8, 0.05)
Text_size = 3
Solution_text_factor = 1.05

###
# PARAMETERS TO INITIALISE THANKS TO FASTA FILE
Sequence_Length = None
Width = None
Height = None
Nucleotide = None
Sequence_per_page = None

#CODE###########################################################################

###
# PARSING

#******************************************************************************#
# Function: parse python arguments
# Params: None
# Return: Argparse object
#******************************************************************************#
def parsing () :
  parser = \
    argparse.ArgumentParser(\
      description="Python3 Script creating puzzle pieces from FASTA file",\
      epilog="Required: Argparse", \
      prog="Returned a PDF file containing puzzle pieces")

  #****************************************************************************#
  # FASTA
  #****************************************************************************#
  parser.add_argument("-fasta", "--FASTA", \
  	help="Input fasta filename", \
  	required=True, \
  	type=str)

  #****************************************************************************#
  # PDF
  #****************************************************************************#
  parser.add_argument("-pdf", "--PDF", \
  	help="Output pdf filename", \
  	required=True, \
  	type=str)

  #****************************************************************************#
  # REVERSE COMPLEMENT
  #****************************************************************************#
  parser.add_argument("--reverse", \
    action='store_true', \
    default=False, \
    help="Add the reverse complement of each sequence.")

  args = parser.parse_args()
  return args

###
# BIO-INFORMATICS ALGORITHMS

#******************************************************************************#
# Function: main function executing the project
# Params: None
# Return: None
#******************************************************************************#
def reverse_complement (seq) :
    complement = {'A': 'T', 'G': 'C', 'T': 'A', 'C': 'G'}
    rev_seq = ''
    for n in seq :
        n = n.upper()
        rev_seq = complement[n] + rev_seq
    return rev_seq

###
# BASIC DRAWING FUNCTIONS

#******************************************************************************#
# Function: main function executing the project
# Params: None
# Return: None
#******************************************************************************#
def draw_stripes (x, y, w, h, dir, n, col) :
    stripe_offset = w / (n + 1)
    top_x = x + (0 if dir == 'B' else stripe_offset)
    bottom_x = x + (0 if dir == 'T' else stripe_offset)
    stripes = f'\t\t\t<g type="stripes" direction="{dir}">\n'
    for _ in range(n + 1) :
        line = f'\t\t\t\t<line x1="{top_x}" y1="{y}" ' \
            + f'x2="{bottom_x}" y2="{y + h}" ' \
            + f'style="stroke:{col};stroke-width:0.5" />\n'
        stripes = stripes + line
        top_x = top_x + stripe_offset
        bottom_x = bottom_x + stripe_offset
    stripes = stripes + '\t\t\t</g>\n'
    return stripes

#******************************************************************************#
# Function: main function executing the project
# Params: None
# Return: None
#******************************************************************************#
def draw_color_indication (x, y, col) :
    indication_width = Nucleotide[0] * Indication[0]
    indication_height = Nucleotide[1] * Indication[1] * 2
    indication_padding = (Nucleotide[0] - indication_width) / 2
    number_of_stripes = 8
    s = draw_stripes(x + indication_padding, y, indication_width, \
        indication_height, 'T', number_of_stripes, col)
    s = s + draw_stripes(x + indication_padding, \
        y + Nucleotide[1] - indication_height, indication_width, \
        indication_height, 'B', number_of_stripes, col)
    return s

#******************************************************************************#
# Function: main function executing the project
# Params: None
# Return: None
#******************************************************************************#
def draw_A (x, y) :
    # '<polygon points="5 5, 45 5, 45 45, 5 45" style="fill:blue"/>'
    col = draw_color_indication(x, y, 'blue')
    padding = (Nucleotide[0] * Nucleotide[2], Nucleotide[1] * Nucleotide[2])
    x1 = padding[0] * 2
    x2 = Nucleotide[0] - padding[0] * 2
    y1 = 2 * padding[1]
    y2 = Nucleotide[1] - 2 * padding[1]
    A = f'\t\t\t<polygon points="{x + x1} {y + y1}, {x + x2} {y + y1}, '\
        + f'{x + x2} {y + y2}, {x + x1} {y + y2}" style="fill:blue"/>'
    return '\t\t<g type="Nucleotide" value="A">\n' + col + A + '\n\t\t</g>'

#******************************************************************************#
# Function: main function executing the project
# Params: None
# Return: None
#******************************************************************************#
def draw_C (x, y) :
    # '<polygon points="5 45, 25 5, 45 45" style="fill:yellow"/>'
    col = draw_color_indication(x, y, 'orange')
    padding = (Nucleotide[0] * Nucleotide[2], Nucleotide[1] * Nucleotide[2])
    x1 = padding[0]
    x2 = Nucleotide[0] - padding[0]
    x3 = Nucleotide[0] / 2
    y1 = 2 * padding[1]
    y2 = Nucleotide[1] - 2 * padding[1]
    C = f'\t\t\t<polygon points="{x + x1} {y + y2}, {x + x3} {y + y1}, ' \
        + f'{x + x2} {y + y2}" style="fill:orange"/>'
    return '\t\t<g type="Nucleotide" value="C">\n' + col + C + '\n\t\t</g>'

#******************************************************************************#
# Function: main function executing the project
# Params: None
# Return: None
#******************************************************************************#
def draw_T (x, y) :
    # '<polygon points="10 25, 25 5, 40 25, 25 45" style="fill:red"/>'
    col = draw_color_indication(x, y, 'red')
    padding = (Nucleotide[0] * Nucleotide[2], Nucleotide[1] * Nucleotide[2])
    x1 = padding[0] * 2
    x2 = Nucleotide[0] - padding[0] * 2
    x3 = Nucleotide[0] / 2
    y1 = 2 * padding[1]
    y2 = Nucleotide[1] - 2 * padding[1]
    y3 = Nucleotide[1] / 2
    T = f'\t\t\t<polygon points="{x  + x1} {y + y3}, {x + x3} {y + y1}, ' \
        + f'{x + x2} {y + y3}, {x + x3} {y + y2}" style="fill:red"/>'
    return '\t\t<g type="Nucleotide" value="T">\n' + col + T + '\n\t\t</g>'

#******************************************************************************#
# Function: main function executing the project
# Params: None
# Return: None
#******************************************************************************#
def draw_G (x, y) :
    # '<circle cx="25" cy="25" r="22.5" style="fill:green" />'
    col = draw_color_indication(x, y, 'green')
    padding = (Nucleotide[0] * Nucleotide[2], Nucleotide[1] * Nucleotide[2])
    x1 = Nucleotide[0] / 2
    y1 = Nucleotide[1] / 2
    r = (Nucleotide[0] - padding[1] * 2) / 2
    G = f'\t\t\t<circle cx="{x + x1}" cy="{y + y1}" r="{r}" '\
        + f'style="fill:green" />'
    return '\t\t<g type="Nucleotide" value="G">\n' + col + G + '\n\t\t</g>'

#******************************************************************************#
# Function: main function executing the project
# Params: None
# Return: None
#******************************************************************************#
def draw (Nucleotide, x, y) :
    if Nucleotide.lower() == 'a' :
        return draw_A(x, y)
    elif Nucleotide.lower() == 'c' :
        return draw_C(x, y)
    elif Nucleotide.lower() == 't' :
        return draw_T(x, y)
    elif Nucleotide.lower() == 'g' :
        return draw_G(x, y)
    else :
        raise f'Unknown Nucleotide : {Nucleotide}'

#******************************************************************************#
# Function: main function executing the project
# Params: None
# Return: None
#******************************************************************************#
def draw_sequence (sequence, offset_x, offset_y) :
    s = ""
    x = 0
    for nucleo in sequence :
        off_x = offset_x + x * Nucleotide[0]
        off_y = offset_y
        s = s + '\n' + draw(nucleo, off_x, off_y)
        x = x + 1
    return s

###
# COMPLEX DRAWING FUNCTIONS

#******************************************************************************#
# Function: main function executing the project
# Params: None
# Return: None
#******************************************************************************#
def draw_cartouche (content, offset_x, offset_y, ident='', color='black'):

    # Compute coordinates
    width_id = Nucleotide[0] * Identifiant
    x1 = offset_x
    x2 = offset_x + Nucleotide[0] * (Sequence_Length + Identifiant)
    x3 = offset_x + width_id / 2
    x4 = offset_x + Nucleotide[0] * (Sequence_Length + 2 * Identifiant)
    y1 = offset_y
    y2 = offset_y + Nucleotide[1]
    y3 = offset_y + Nucleotide[1] / 2

    # Define the 'cartouche'
    background = f'\t<polygon points="{x1} {y1}, {x2} {y1}, ' \
        + f'{x2} {y2}, {x1} {y2}"  fill="white" stroke="none" ' \
        + f'stroke-width="1"/>\n'

    cartouche = f'\t<polygon points="{x1} {y1}, {x4} {y1}, ' \
        + f'{x4} {y2}, {x1} {y2}"  fill="none" stroke="black" ' \
        + f'stroke-width="1"/>\n'

    ident_block = f'\t<rect x="{x1}" y="{y1}" width="{width_id}" ' \
        + f'height="{Nucleotide[1]}" stroke="black" stroke-width="0" ' \
        + f'fill="{color}"/>\n'

    ident = f'\t<text x="{x3}" y="{y3}" dominant-baseline="middle" ' \
        + f'text-anchor="middle" fill="white" font-size="{Text_size}">' \
        + f'{ident}</text>\n'

    arrow_block = f'\t<rect x="{x2}" y="{y1}" width="{width_id}" ' \
        + f'height="{Nucleotide[1]}" stroke="black" stroke-width="0.5" ' \
        + f'fill="white"/>\n'

    arrow = f'\t<polygon points="{x2+1} {y1+1}, {x4-1} {y3}, {x2+1} {y2-1}" ' \
        + f'fill="black" stroke-width="0"/>\n'

    svg = f'<g type="piece">\n' \
        + background \
        + ident_block \
        + ident \
        + content \
        + arrow_block \
        + arrow \
        + cartouche \
        + '</g>\n'

    return svg

#******************************************************************************#
# Function: main function executing the project
# Params: None
# Return: None
#******************************************************************************#
def draw_piece \
    (ident, sequence, offset_x, offset_y, color='black', reverse=False):

    Y = offset_y
    X = offset_x + Nucleotide[0] * Identifiant # if not reverse else offset_x

    if reverse :
        sequence = reverse_complement(sequence)

    sequence_svg = '\t<g type="sequence">' \
        + draw_sequence(sequence, X, Y) \
        + '\n\t</g>\n'

    ID = (f'{ident}{"F" if not reverse else "R"}') if len(ident) != 0 else ''

    svg = draw_cartouche (sequence_svg, offset_x, offset_y, \
        ident=ID, color=color)

    return svg

#******************************************************************************#
# Function: main function executing the project
# Params: None
# Return: None
#******************************************************************************#
def draw_solution (solutions, offset_x, offset_y):
    # Compute the solution string
    s = ''
    for solution in solutions :
        s = s + solution + ' | '
    s = s.strip(' | ')

    # Compute some coordinates
    Y = offset_y + Nucleotide[1] / 2
    X = (offset_x + Nucleotide[0] * Identifiant + offset_x + Nucleotide[0] \
        * (Sequence_Length + Identifiant)) / 2

    solution_svg = f'\t<text x="{X}" y="{Y}" ' \
        + f'dominant-baseline="middle" text-anchor="middle" fill="black" ' \
        + f'font-size="{Text_size * Solution_text_factor}" ' \
        + f'font-weight="bold">{s}</text>\n'

    svg = draw_cartouche(solution_svg, offset_x, offset_y)

    return svg


def svg_format (s) :
    return \
        f'<svg viewBox="0 0 {A4[0]} {A4[1]}" version="1.1" ' \
        + f'xmlns="http://www.w3.org/2000/svg">\n' \
        + s \
        + f'</svg>'

###
# MAIN DRAWING FUNCTIONS

#******************************************************************************#
# Function: main function executing the project
# Params: None
# Return: None
#******************************************************************************#
def init_global_parameters (fasta):
    global Sequence_Length
    global Width
    global Height
    global Nucleotide
    global Sequence_per_page

    Sequence_Length = fasta['Sequence_Length']
    Width = (A4[0] - A4_margin[0] * 2) / (Sequence_Length + 2 * Identifiant)
    Height = Width * 1.2
    Nucleotide = (Width, Height, 0.075)
    Sequence_per_page = math.floor((A4[1] - 2 * A4_margin[1]) / Height)

#******************************************************************************#
# Function: main function executing the project
# Params: None
# Return: None
#******************************************************************************#
def draw_fasta_sequences (fasta, withReverse=False):
    Sequences = fasta['Sequences']
    SVGs = []
    while len(Sequences) > 0:
        Current_page = Sequences[:Sequence_per_page]
        offset_x = A4_margin[0]
        offset_y = A4_margin[1]
        SVG = ''
        for (ident, sequence) in Current_page :
            SVG = SVG \
                + draw_piece(ident, sequence, offset_x, offset_y, color='black')
            offset_y = offset_y + Nucleotide[1]
        SVGs.append(svg_format(SVG))
        if withReverse:
            offset_x = A4_margin[0]
            offset_y = A4_margin[1]
            SVG_R = ''
            for (ident, sequence) in Current_page :
                SVG_R = SVG_R \
                    + draw_piece(ident, sequence, offset_x, offset_y, \
                    color='black', reverse=True)
                offset_y = offset_y + Nucleotide[1]
            SVGs.append(svg_format(SVG_R))
        Sequences = Sequences[Sequence_per_page:]
    return SVGs

#******************************************************************************#
# Function: main function executing the project
# Params: None
# Return: None
#******************************************************************************#
def draw_fasta_complements (fasta):
    offset_x = A4_margin[0]
    offset_y = A4_margin[1]
    Solution = draw_solution(fasta['Solution'], offset_x, offset_y)
    offset_y = offset_y + Nucleotide[1]
    Input = draw_piece('', fasta['IO'][0], offset_x, offset_y, color='green')
    offset_y = offset_y + Nucleotide[1]
    Output = draw_piece('', fasta['IO'][1], offset_x, offset_y, color='red')
    SVG = Solution + Input + Output
    return svg_format(SVG)

#******************************************************************************#
# Function: main function executing the project
# Params: None
# Return: None
#******************************************************************************#
def draw_fasta (fasta, withReverse=False):
    init_global_parameters(fasta)
    SVGs = draw_fasta_sequences(fasta, withReverse=withReverse)
    SVGs.append(draw_fasta_complements(fasta))
    return SVGs

###
# FILE PROCESSING

#******************************************************************************#
# Function: main function executing the project
# Params: None
# Return: None
#******************************************************************************#
def read_fasta_header (header):
    # line format : '> ID:<id>|POS:<rank_1>/<size>;...;<rank_n>/<size>|REP:<n>'
    # or
    # line format : '> FIRST' '> LAST'
    if 'FIRST' in header.upper() or 'LAST' in header.upper() :
        ID = header.strip('>').strip()
        return {'ID':ID, 'POS':None, 'SIZE':None, 'REP':None}
    else :
        split_s = header[1:].strip().split('|')
        ID = split_s[0].split(':')[1]
        POSs = split_s[1].split(':')[1].split(';')
        SIZE = None
        POS = []
        for p in POSs :
            p_split = p.split('/')
            POS.append((int(p_split[0][:-1]), ID + p_split[0][-1]))
            SIZE = int(p_split[1])
        REP = int(split_s[2].split(':')[1])
        return {'ID':ID, 'POS':POS, 'SIZE':SIZE, 'REP':REP}

#******************************************************************************#
# Function: main function executing the project
# Params: None
# Return: None
#******************************************************************************#
def read_fasta_file (filename):
    with open(filename, 'r') as file :
        current_header = None
        fasta = { \
            'Sequence_Length': None, \
            'Sequences': [], \
            'Solution': [], \
            'IO': [None, None] \
        }
        for l in file.readlines() :
            if len(l) == 0 or l[0] == '#':
                pass
            l = l.strip()
            if l[0] == '>' :
                current_header = read_fasta_header(l)
                if current_header['ID'] not in ['FIRST', 'LAST']:
                    if len(fasta['Solution']) == 0 :
                        fasta['Solution'] = [None] * current_header['SIZE']
                    for (POS, ID) in current_header['POS'] :
                        fasta['Solution'][POS - 1] = ID
            else :
                if current_header == None :
                    raise f"An error occure: no HEADER associated " \
                        + f"with the sequence: {l}"
                ID = current_header['ID'].upper()
                REP = current_header['REP']
                if fasta['Sequence_Length'] is not None :
                    assert \
                        (fasta['Sequence_Length'] == len(l))
                else :
                    fasta['Sequence_Length'] = len(l)
                if ID == 'FIRST' :
                        fasta['IO'][0] = l
                elif ID == 'LAST' :
                        fasta['IO'][1] = l
                else :
                    while REP > 0 :
                        fasta['Sequences'].append((ID, l))
                        REP = REP - 1
                current_header = None
    return fasta

###
# OUTPUT PROCESSING

#******************************************************************************#
# Function: main function executing the project
# Params: None
# Return: None
#******************************************************************************#
def svg2pdf (svg_file, pdf_file) :
    cmd = [ \
        'inkscape', \
        f'{svg_file}', \
        '--export-area-page', \
        '--without-gui', \
        f'--export-pdf={pdf_file}' \
    ]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    proc.communicate()

#******************************************************************************#
# Function: main function executing the project
# Params: None
# Return: None
#******************************************************************************#
def mergePDF (pdf_files, output_file) :
    cmd = ['pdfjam'] + pdf_files + ['-o', f'{output_file}']
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    proc.communicate()

#******************************************************************************#
# Function: main function executing the project
# Params: None
# Return: None
#******************************************************************************#
def clear () :
    shutil.rmtree(Current_path + '/.temp')

###
# MAIN FUNCTION

#******************************************************************************#
# Function: main function executing the project
# Params: None
# Return: None
#******************************************************************************#
def main ():
    if not os.path.exists(SVG_path):
        os.makedirs(SVG_path)
    if not os.path.exists(PDF_path):
        os.makedirs(PDF_path)

    args = parsing()

    input_file = args.FASTA
    output_file = args.PDF

    filename = input_file.split('/')[-1].rsplit('.', 1)[0]
    fasta = read_fasta_file(input_file)
    svgs = draw_fasta(fasta, withReverse=args.reverse)
    pdfs = []
    for i in range(len(svgs)) :
        current_svg_file = SVG_path + filename + f'_{i}.svg'
        current_pdf_file = PDF_path + filename + f'_{i}.pdf'
        with open(current_svg_file, 'w') as svg_file :
            svg = svgs[i]
            svg_file.write(svg)
        svg2pdf(current_svg_file, current_pdf_file)
        pdfs.append(current_pdf_file)

    mergePDF(pdfs, output_file)
    clear()

#RUN############################################################################
if __name__ == '__main__' :
  main()
