from imgs import create_card_list
from generator import generate
import json
import sys
import os
from getopt import getopt, GetoptError

def get_path(path):
    if path[-1:] != '/':
        path += '/'
    return path

# Save generated images in directory
def gen_cards_file(outdir, cards, dir):
    imgs = create_card_list(cards, dir)

    i = 1
    for im in imgs:
        path = outdir + str(i) + ".png"
        im.save(path)
        i += 1

# Print generated cards in text output
def pretty_print_card(cards):
    i = 1
    for c in cards:
        print("Card :", i)
        for a in c:
            print("\t", a, ":", c[a])
        i += 1

# Print the help message
def print_help():
    print("Generate a list of images following a list of attributes")
    print("Arguments:")
    print("\t-a [FILE] : Path to the list of attributes file")
    print("\t-d [DIR] : Path to the attributes directory (. by default)")
    print("\t-m [FILE] : Path to the attributes model file")
    print("\t-o [DIR] : Output directory (optional) of the genereted images")
    print("\t-s [SEED] : Random generator seed (optional)")
    print("\t-h : Print this message")

# Generate card game
# -a : attribute file
# -d : relative attributes directory (for files)
# -m : model file
# [-o] : output directory for images (with / at the end), if not specified cards will be printed in standard output
# [-s] : RNG seed
def main(argv):
    try:
        opts, args = getopt(argv, "ha:m:o:s:d:")
        if len(opts) == 0:  # No arguments -> error
            print_help()
            sys.exit(0)

        attributes = ""
        model = ""
        seed = None
        outdir = None
        reldir = "."

        for opt, arg in opts:
            if opt == "-a": #attributes file
                attributes = json.load(open(arg))
                att_path = arg
            elif opt == "-m": # model file
                model = json.load(open(arg))
            elif opt == "-o": # Output directory
                outdir = arg
            elif opt == "-s": # Given RNG seed
                seed = arg
            elif opt == '-d': # relative attributes directory
                reldir = arg
            elif opt == '-h':
                print_help()
                sys.exit(0)

        # Generate cards
        cards = generate(attributes, model, seed)

        # output in files
        if outdir != None:
            outdir = get_path(outdir)
            if not os.path.isdir(outdir):
                os.mkdir(outdir)

            reldir = get_path(reldir)

            gen_cards_file(outdir, cards, reldir)
        else: # pretty print
            pretty_print_card(cards)

    except GetoptError:
        print_help()
    except FileNotFoundError:
        print("File not found")

if __name__=='__main__':
    main(sys.argv[1:])
