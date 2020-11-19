# This file collect all parameters for the human puzzle generator.
# They are ordered from the one you want to change to the one you don't want to
# hear about.

# SENTENCES is the list of sentence used, one for each puzzle.
# This is the main paramater you want to change to have different puzzle.
NAME_PUZZLES = "tailleur"

SENTENCES = []
SENTENCES.append("Un tailleur est importuné par des nuées de mouches lors de son repas. Il donne un coup de torchon pour protéger sa tartine, et écrase sept mouches d'un coup.")
SENTENCES.append("Fier de son exploit, il brode «sept d'un coup» sur sa ceinture. Il part visiter le monde, avec en poche un morceau de fromage et un oiseau vivant.")
SENTENCES.append("Il rencontre un géant, qui en voyant la ceinture croit que le tailleur a tué sept hommes d'un coup. Impressionné, le géant décide de le mettre à l'épreuve.")
SENTENCES.append("Le géant presse une roche jusqu'à en tirer de l'eau. Le tailleur fait croire au géant que son fromage est une pierre, puis l'écrase jusqu'à en tirer du jus.")
SENTENCES.append("Le géant lance une pierre de toutes ses forces. Elle finit par retomber très loin. Le tailleur lance son oiseau, qui s'envole et disparait au loin sans retomber.")
SENTENCES.append("La nuit, le géant veut tuer le tailleur en tapant dans son lit. Mais le tailleur dormait par terre et quand il apparait au matin, le géant s'enfuit effrayé.")
SENTENCES.append("Le roi demande au tailleur de tuer deux géants. Le tailleur lance des petites pierres sur deux géants qui font la sieste. La dispute dégénère et les géants s'entretuent.")
SENTENCES.append("Le roi lui demande de capturer une licorne, puis un sanglier. Le tailleur est rusé : la licorne plante sa corne dans un arbre; le sanglier s'enferme dans une chapelle.")
SENTENCES.append("Le roi est inquiet et veut le faire tuer. Le tailleur prétend parler dans son sommeil pour effrayer les serviteurs qui s'enfuient. Il peut alors épouser la princesse.")


# SHAPE specify the (number of lines, number of columns) of the puzzle.
# Multiplication of the two terms gives the number of pieces of your puzzle.
# Adapt it to the number of player you have!
SHAPE = (4,7)

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
