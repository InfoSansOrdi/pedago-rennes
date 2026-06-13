import numpy as np
from enum import Enum
from PIL import Image, ImageDraw


Red = [255, 0, 0]
Green = [0, 255, 0]
Blue = [0, 0, 255]
Black = [0, 0, 0]
White = [255, 255, 255]

Colors = [Red, Green, Blue, Black, White]

class IterType(Enum):
    CoordIter = 0
    CellIter = 1

class Grid:

    cell_nb = 6
    cell_size = 200

    color_matrix = []

    iterator_index = (0, 0)
    iterator_type = IterType.CoordIter
    
    def __init__(self, cell_nb = 6, cell_size = 200):
        self.cell_nb = cell_nb
        self.cell_size = cell_size
        self.color_matrix = 255 * np.ones((cell_nb, cell_nb, 3), int)

    def __str__(self):
        return self.color_matrix.__str__()

    def __iter__(self):
        self.iterator_index = (-1, self.cell_nb)
        return self

    def __next__(self):

        '''
        La valeur de retour dépend du choix du type d'itérator!
        Un CellIter renverra chaque case (liste RGB) alors qu'un
        CoordIter renverra les couples (ligne, colonne) dans l'ordre lexicographique
        '''

        lin, col = self.iterator_index
        if(col + 1 >= self.cell_nb):
            if(lin + 1 >= self.cell_nb):
                raise StopIteration
            else:
                self.iterator_index = (lin + 1, 0)
                if(self.iterator_type == IterType.CoordIter):
                    return self.iterator_index
                elif(self.iterator_type == IterType.CellIter):
                    return self.color_matrix[lin + 1, 0]
        else:
            self.iterator_index = (lin, col + 1)
            if(self.iterator_type == IterType.CoordIter):
                    return self.iterator_index
            elif(self.iterator_type == IterType.CellIter):
                    return self.color_matrix[lin, col + 1]


    def set_iter_type(self, iter_type):
        self.iterator_type = iter_type

    def make_image(self):
        outline_size = int(self.cell_size / 100)
        grid_sep_size = int(outline_size / 2)
        total_size = 2 * (outline_size - grid_sep_size) + self.cell_nb * (self.cell_size + grid_sep_size)
        new_image = Image.new('RGB', (total_size, total_size))

        draw_obj = ImageDraw.Draw(new_image)
        draw_obj.rectangle([(0, 0), (total_size, outline_size)], fill = "#000000", outline = None)
        draw_obj.rectangle([(0, 0), (outline_size, total_size)], fill = "#000000", outline = None)
        draw_obj.rectangle([(total_size - outline_size, outline_size), (total_size, total_size)], fill = "#000000", outline = None)
        draw_obj.rectangle([(outline_size, total_size - outline_size), (total_size, total_size)], fill = "#000000", outline = None)
        
        self.set_iter_type(IterType.CoordIter)

        for lin, col in iter(self):
            first_coord = ((outline_size + col * (self.cell_size + grid_sep_size)), (outline_size + lin * (self.cell_size + grid_sep_size)))
            second_coord = (first_coord[0] + self.cell_size, first_coord[1] + self.cell_size)
            coord_list = [first_coord, second_coord]
            draw_obj.rectangle(coord_list, fill = tuple(self.color_matrix[lin, col]), outline="#000000")


        return new_image

    def plot_pixel(self, x, y, color):
        try:
            self.color_matrix[y, x] = color
        except IndexError:
            print("plot_pixel -> Invalid Coordinates (" + str(x) + ", " + str(y) + ")")

        return self
    
    def fill_grid(self, color):
        self.iterator_type = IterType.CoordIter
        for lin, col in iter(self):
            self.color_matrix[lin, col] = color

        return self

    def plot_horizontal_line(self, begin_coord, end_coord, color):
        for index in range (begin_coord[0], end_coord[0] + 1):
            self.plot_pixel(index, begin_coord[1], color)

        return self

    def plot_vertical_line(self, begin_coord, end_coord, color):
        for index in range (begin_coord[1], end_coord[1] + 1):
            self.plot_pixel(begin_coord[0], index, color)

        return self

    def plot_diagonal_line(self, begin_coord, end_coord, color):

        if (np.abs(end_coord[0] - begin_coord[0]) != np.abs(end_coord[1] - begin_coord[1])):
            print("plot_diagonal_line -> Must be a 45° Diagonal!")
            return self
        
        else:
            cur_x = begin_coord[0]
            cur_y = begin_coord[1]
            for _ in range(np.abs(end_coord[0] - begin_coord[0]) + 1):
                self.plot_pixel(cur_x, cur_y, color)
                if(end_coord[0] >= begin_coord[0]):
                    cur_x += 1
                else:
                    cur_x -= 1
                
                if(end_coord[1] >= begin_coord[1]):
                    cur_y += 1
                else:
                    cur_y -= 1

            return self

    def flip_horizontal(self):
        self.color_matrix = np.flip(self.color_matrix, 1)
        return self

    def flip_vertical(self):
        self.color_matrix = np.flip(self.color_matrix, 0)
        return self
