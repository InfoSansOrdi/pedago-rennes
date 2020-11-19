# This file collect all parameters for the human puzzle generator.
# They are ordered from the one you want to change to the one you don't want to
# hear about.

# SENTENCES is the list of sentence used, one for each puzzle.
# This is the main paramater you want to change to have different puzzle.
NAME_PUZZLES = "duchesse"

SENTENCES = []
SENTENCES.append("Bonjour, je suis un gentil puzzle, en plus cette fois-ci je passe sur du 3x3.")
SENTENCES.append("Ces chaussettes de l'archiduchesse sont-elles sèches ou archi sèches ?")


# SHAPE specify the (number of lines, number of columns) of the puzzle.
# Multiplication of the two terms gives the number of pieces of your puzzle.
# Adapt it to the number of player you have!
SHAPE = (3,3)

# NUMBERS_ON_BORDER set to False makes border of the puzzle identifiable by
# putting no number on it.
# Set it to True to make the exercise more difficult, border will have lone
# number without matching piece.
NUMBERS_ON_BORDER = False



# The final output of the script
OUTPUT_FOLDER = "output-" + NAME_PUZZLES + "/"
OUTPUT_FOLDER_INDIVIDUAL_PDF = OUTPUT_FOLDER + "individual_puzzles/"
OUTPUT_PDF = OUTPUT_FOLDER + NAME_PUZZLES + ".pdf"
OUTPUT_INDIVIDUAL_PDFs = OUTPUT_FOLDER_INDIVIDUAL_PDF + "puzzle_"

# SVG_TEMPLATE_FILENAME is the path to the svg file used as template to generate
SVG_TEMPLATE_FRONT_FILENAME = "templates/inputpuzzle.svg"
SVG_TEMPLATE_BACK_FILENAME = "templates/inputpuzzleback.svg"

# The TMP folders used to generate the final output
TMP_FOLDER = "tmp/"
TMP_FOLDER_INDIVIDUAL_PUZZLES = TMP_FOLDER + "individual_puzzles/"
TMP_OUTPUT_SVG = TMP_FOLDER + "puzzle"
TMP_OUTPUT_INDIVIDUAL_PUZZLE_PDF = TMP_FOLDER_INDIVIDUAL_PUZZLES + "puzzle_"
