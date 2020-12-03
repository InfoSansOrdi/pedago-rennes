from random import randint, shuffle, seed
from config import *
import glob
import os

def main() :
	print("Welcome to the human puzzle generator v2!")
	print("Generating puzzles with following parameters:")
	print("SENTENCES:")
	print("---")
	print(SENTENCES)
	print("---")
	print("SHAPE:", SHAPE[0], "lines and", SHAPE[1], "columns (" + str(SHAPE[0]*SHAPE[1]) + " pieces)")
	print("NUMBERS ON BORDER:", NUMBERS_ON_BORDER)
	print("Working...")
	generate_architecture()
	for (i,sentence) in enumerate(SENTENCES) : 
		hash = hash_puzzle(sentence)
		generate_svg(sentence, SHAPE, hash)
		generate_pdfs_from_svg()
		merge_pdfs_to_create_individual_puzzle(i, hash)
		delete_tmp_files()
	merge_individuals_puzzle_to_create_final_puzzle()
	delete_single_pdfs()
	print("Done. Check the result in '"+ OUTPUT_PDF + "'.")


def generate_architecture() : 
	try:
		os.system("mkdir " + TMP_FOLDER + " 2>/dev/null")
		os.system("mkdir " + TMP_FOLDER_INDIVIDUAL_PUZZLES + " 2>/dev/null")
		os.system("mkdir " + OUTPUT_FOLDER + " 2>/dev/null")
		os.system("mkdir " + OUTPUT_FOLDER_INDIVIDUAL_PDF + " 2>/dev/null")
	except:
		raise Exception("Cannot create some folder")



# Returns the index of the minimal element in the iterable.
def argmin(iterable):
	(min_value, argmin_index) = min([(a, b) for (b, a) in enumerate(iterable)])
	return argmin_index

# Modify `words` so that the words at index `first` is merged with the next item
# with `sep` as separator.
# `first` should be lower than `len(words) - 1` (so `len(words)` should be > 1).
def fusion(words, first, sep=" "):
	words[first] = words[first] + sep + words[first + 1]
	del words[first+1]

# Seeds the random number generator with puzzle parameter, and return a unique
# hash for those parameters.
def hash_puzzle(sentence):
	seed(sentence + str(SHAPE) + str(NUMBERS_ON_BORDER) + str(MIN_NUMBER_PIECE) + str(MAX_NUMBER_PIECE))
	random_number = randint(100000, 1000000)
	return get_identifier_puzzle_from_hash(random_number)

# Given a string `sentence`, splits it into a list of `number_pieces` strings.
# Separations are made only where `sep` appears.
# The function tries to egalizes finals strings lengths.
# Algorithm used: greedy.
def repartition(nb_pieces, sentence, sep=" "):
	words = sentence.split(sep)
	special_caracters = [":", ";", "?", "!"]
	for (index, w) in enumerate(words):
		if w in special_caracters:
			fusion(words, index - 1, sep=sep)
	if len(words) < nb_pieces:
		raise Exception("Not enough words for " + str(nb_pieces) + " pieces.")
	while len(words) > nb_pieces:
		pair_lengths = [len(words[i]+words[i+1]) for i in range(len(words)-1)]
		min_length_index = argmin(pair_lengths)
		fusion(words, min_length_index, sep=sep)
	return words


# [MIN_NUMBER_PIECE, MAX_NUMBER_PIECE] is the range among which numbers are
# randomly picked to set the value of puzzle pieces edges.
MIN_NUMBER_PIECE = 1
MAX_NUMBER_PIECE = SHAPE[0] * SHAPE[1] * 4
def random_piece_number(already_used) :
	all_numbers = range(MIN_NUMBER_PIECE, MAX_NUMBER_PIECE+1)
	forbidden_numbers = [n for n in all_numbers if ("6" in str(n) or "9" in str(n))]
	free_numbers = [n for n in all_numbers if n not in already_used and n not in forbidden_numbers]
	if len(free_numbers) == 0:
		raise(Exception("All pieces numbers used!"))
	else:
		random_index = randint(0, len(free_numbers)-1)
		new_number = free_numbers[random_index]
		already_used.append(new_number)
		return new_number


def get_metadata_pieces(id_puzzle, nb_pieces) :
	numbers_on_back = list(range(1, nb_pieces+1))
	shuffle(numbers_on_back)
	metadata = []
	for n in numbers_on_back:
		number = "{}/{}".format(n, nb_pieces)
		metadata.append([number, id_puzzle])
	if nb_pieces%2 == 1 :
		metadata.append(["spare", "spare"])
	return metadata

def get_identifier_puzzle_from_hash(hash):
	bonus = 32 * NUMBERS_ON_BORDER

	nb_1 = (hash%26) + bonus
	nb_2 = ((hash//26)%26) + bonus
	nb_3 = (((hash//26)//26)%26) + bonus

	return chr(65 + nb_1) + chr(65 + nb_2) + chr(65 + nb_3)


tmp_files_to_delete = []
puzzles_to_delete = []
def generate_svg(sentence, shape, hash, sep=" "):
	try:
		svg_template_front = open(SVG_TEMPLATE_FRONT_FILENAME, "r").read()
		svg_template_back = open(SVG_TEMPLATE_BACK_FILENAME, "r").read()
	except:
		raise Exception("Cannot find svg template at path: " + SVG_TEMPLATE_FRONT_FILENAME + " or " + SVG_TEMPLATE_BACK_FILENAME)

	words = repartition(shape[0] * shape[1], sentence, sep)
	numbers_pieces = assign_numbers_to_pieces(shape)
	if(not NUMBERS_ON_BORDER):
		remove_borders(shape, numbers_pieces)
	metadata = get_metadata_pieces(hash, len(words))

	if len(words)%2 == 1:
		words.append("")
		numbers_pieces.append(["","","",""])

	svg_pages_front = []
	svg_pages_back = []
	for i in range(0,len(words),2):
		svg_front = svg_template_front
		svg_back = svg_template_back

		(top_nb, bottom_nb, right_nb, left_nb) = numbers_pieces[i]
		svg_front = svg_front.replace("TXT1", words[i]).replace("1h", top_nb).replace("1b", bottom_nb).replace("1d", right_nb).replace("1g", left_nb)

		(top_nb, bottom_nb, right_nb, left_nb) = numbers_pieces[i+1]
		svg_front = svg_front.replace("TXT2", words[i+1]).replace("2h", top_nb).replace("2b", bottom_nb).replace("2d", right_nb).replace("2g", left_nb)

		svg_pages_front.append(svg_front)

		svg_back = svg_back.replace("TXT1", metadata[i][0])
		svg_back = svg_back.replace("TXT2", metadata[i+1][0])

		svg_back = svg_back.replace("META", metadata[i][1])

		svg_pages_back.append(svg_back)

	for i in range(len(svg_pages_front)):
		svg_page_front = svg_pages_front[i]
		svg_page_back = svg_pages_back[i]
		name_output_front = TMP_OUTPUT_SVG + "_front_" + str(i) + "_" + hash + ".svg"
		name_output_back = TMP_OUTPUT_SVG + "_back_" + str(i) + "_" + hash + ".svg"
		output_front = open(name_output_front, "w")
		output_back = open(name_output_back, "w")
		tmp_files_to_delete.append(name_output_front)
		tmp_files_to_delete.append(name_output_back)
		output_front.write(svg_page_front)
		output_back.write(svg_page_back)
		output_front.close()
		output_back.close()
		# print("writing " + name_output)



def generate_pdfs_from_svg():
	svgs = glob.glob(TMP_FOLDER + "*.svg")
	for svg in svgs:
		pdf_name = svg.replace("svg", "pdf")
		command_svg_to_pdf = "inkscape {name_svg} --export-area-page --without-gui --export-pdf={name_pdf}".format(name_svg=svg, name_pdf=pdf_name)
		os.system(command_svg_to_pdf)
		tmp_files_to_delete.append(pdf_name)


def merge_pdfs_to_create_individual_puzzle(nb_puzzle, hash):
	pdfs = glob.glob(TMP_FOLDER + "*.pdf")
	pdfs = sorted(pdfs)
	pdfs_back, pdfs_front = pdfs[:len(pdfs)//2], pdfs[len(pdfs)//2:]
	pdfs_back.sort(key=lambda x: int("".join([c for c in x if c.isdigit()])))
	pdfs_front.sort(key=lambda x: int("".join([c for c in x if c.isdigit()])))
	# print(pdfs_front, pdfs_back)

	command_merge_pdfs = "pdfunite "
	for i in range(0, len(pdfs_front)) :
		command_merge_pdfs += " {page_front} {page_back} ".format(page_front=pdfs_front[i], page_back=pdfs_back[i])
	tmp_output_individual_pdf = TMP_OUTPUT_INDIVIDUAL_PUZZLE_PDF + str(nb_puzzle) + "_" + hash + ".pdf"
	command_merge_pdfs += " {output_name}".format(output_name=tmp_output_individual_pdf)
	return_value = os.system(command_merge_pdfs)
	if return_value != 0 :
		print("Error somewhere when generating some puzzle.")
	puzzles_to_delete.append(tmp_output_individual_pdf)
	individual_pdf_name_in_output = OUTPUT_INDIVIDUAL_PDFs + str(nb_puzzle) + "_" + hash + ".pdf"	
	os.system("cp {} {}".format(tmp_output_individual_pdf, individual_pdf_name_in_output))
	

def merge_individuals_puzzle_to_create_final_puzzle() : 
	pdfs = glob.glob(TMP_OUTPUT_INDIVIDUAL_PUZZLE_PDF + "*.pdf")
	pdfs = sorted(pdfs)
	# print(pdfs_front, pdfs_back)

	command_merge_pdfs = "pdfunite "
	command_merge_pdfs += " ".join(pdfs)
	command_merge_pdfs += " {output_name}".format(output_name=OUTPUT_PDF)
	return_value = os.system(command_merge_pdfs)
	if return_value != 0 :
		print("Error somewhere.")


# Return type:
# List (one for each piece) with (top, bottom, right, left) in each cell.
# top, bottom, right and left are strings representing numbers.
# Intermediate type (the_array) (for shape (3,2)):
#		n 		n
#	n	M1	n	M2	n
#		n		n
#	n	M3	n	M4	n
#		n 		n
#	n	M5	n	M6	n
#		n		n
def assign_numbers_to_pieces(shape):
	the_array = []

	nb_rows_puzzle = shape[0]
	nb_columns_puzzle = shape[1]

	nb_rows_numbers = nb_rows_puzzle*2 + 1
	nb_columns_numbers = nb_columns_puzzle + 1

	currently_vertical = True
	used_numbers = []
	for i in range(nb_rows_numbers):
		the_array.append([])
		for j in range(nb_columns_numbers - currently_vertical):
			n = random_piece_number(used_numbers)
			the_array[i].append(n)

		currently_vertical = not currently_vertical

	the_output = []
	for i in range(nb_rows_puzzle):
		i = i*2 #To match index in the array.
		for j in range(nb_columns_puzzle):
			top = str(the_array[i][j])
			bottom = str(the_array[i+2][j])
			right = str(the_array[i+1][j+1])
			left = str(the_array[i+1][j])
			the_output.append((top, bottom, right, left))

	return the_output


def remove_borders(shape, numbers_on_pieces):
	nb_row, nb_col = shape
	for i in range(nb_col):
		top_piece_index = i
		(top, bot, right, left) = numbers_on_pieces[top_piece_index]
		numbers_on_pieces[top_piece_index] = ("", bot, right, left)

		bot_piece_index = nb_col * (nb_row - 1) + i
		(top, bot, right, left) = numbers_on_pieces[bot_piece_index]
		numbers_on_pieces[bot_piece_index] = (top, "", right, left)

	for i in range(nb_row):
		left_piece_index = i * nb_col
		(top, bot, right, left) = numbers_on_pieces[left_piece_index]
		numbers_on_pieces[left_piece_index] = (top, bot, right, "")

		right_piece_index = i * nb_col + nb_col - 1
		(top, bot, right, left) = numbers_on_pieces[right_piece_index]
		numbers_on_pieces[right_piece_index] = (top, bot, "", left)

def delete_tmp_files() :
	global tmp_files_to_delete
	for filename in tmp_files_to_delete :
		os.system("rm {}".format(filename))
	tmp_files_to_delete = []

def delete_single_pdfs() :
	for filename in puzzles_to_delete :
		os.system("rm {}".format(filename))


if __name__ == '__main__':
	main()