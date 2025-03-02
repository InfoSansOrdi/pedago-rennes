from grid_generator import *
import random




if __name__ == "__main__":

    # Grillage Simple

    g = Grid(cell_nb = 6)

    g.plot_vertical_line((1, 0), (1, 5), Red)
    g.plot_vertical_line((4, 0), (4, 5), Red)

    g.plot_horizontal_line((0, 1), (5, 1), Red)
    g.plot_horizontal_line((0, 4), (5, 4), Red)

    g.plot_diagonal_line((0, 0), (5, 5), White)
    g.plot_diagonal_line((5, 0), (0, 5), White)
    g.make_image().save("grid_facile.png")


    # Montagne

    g = Grid(cell_nb = 6)

    g.plot_diagonal_line((3, 2), (5, 4), Blue)
    g.plot_diagonal_line((3, 1), (5, 3), Blue)
    g.plot_diagonal_line((2, 2), (5, 5), Blue)

    g.plot_diagonal_line((0, 5), (3, 2), Green)
    g.plot_diagonal_line((0, 4), (3, 1), Green)

    g.make_image().save("montagne.png")


    # Aléatoire Total

    g = Grid(cell_nb = 6)

    color_cnt = 0

    for rnd_pixel in range(35):
        x = random.randint(0, 5)
        y = random.randint(0, 5)
        #while(g.color_matrix[y, x, :].tolist() == White): 
        #    x = random.randint(0, 5)
        #    y = random.randint(0, 5)
        g.plot_pixel(x, y, Colors[color_cnt])
        color_cnt = color_cnt + 1 if (color_cnt < 3) else 0

    g.make_image().save("random.png")


    # Forme Penchée

    g = Grid(cell_nb = 6)

    g.plot_horizontal_line((0, 4), (2, 4), Red)
    g.plot_pixel(0, 3, Red)

    g.plot_vertical_line((1, 0), (1, 2), Blue)
    g.plot_pixel(2, 0, Blue)

    g.plot_horizontal_line((3, 1), (5, 1), Green)
    g.plot_pixel(5, 2, Green)

    g.plot_vertical_line((4, 3), (4, 5), Black)
    g.plot_pixel(3, 5, Black)

    g.flip_horizontal()

    g.make_image().save("forme.png")


    # Damier

    g = Grid(cell_nb = 6)

    g.plot_diagonal_line((0, 0), (5, 5), Black)
    g.plot_diagonal_line((2, 0), (5, 3), Black)
    g.plot_diagonal_line((0, 2), (3, 5), Black)
    g.plot_diagonal_line((4, 0), (5, 1), Black)
    g.plot_diagonal_line((0, 4), (1, 5), Black)

    #g.plot_diagonal_line((0, 5), (5, 0), Red)
    #g.plot_diagonal_line((0, 3), (3, 0), Green)
    #g.plot_diagonal_line((2, 5), (5, 2), Green)


    g.make_image().save("damier.png")


    # presque_random

    g = Grid(cell_nb = 6)

    g.plot_diagonal_line((1,0), (3,2), Red)
    g.plot_horizontal_line((3, 0), (5, 0), Red)

    g.plot_pixel(0, 1, Black)
    g.plot_pixel(1, 1, Black)
    g.plot_pixel(0, 2, Black)
    g.plot_pixel(0, 3, Green)
    g.plot_pixel(3, 1, Blue)
    g.plot_pixel(4, 1, Blue)

    g.plot_diagonal_line((2, 2), (4, 4), Blue)
    g.plot_diagonal_line((1, 2), (3, 4), Green)
    g.plot_pixel(4, 2, Green)
    g.plot_pixel(4, 3, Green)

    g.plot_pixel(5, 3, Black)
    g.plot_pixel(5, 4, Black)

    g.plot_pixel(1, 4, Blue)
    g.plot_pixel(1, 5, Blue)

    g.plot_pixel(2, 4, Red)
    g.plot_pixel(2, 5, Red)

    g.plot_pixel(3, 5, Blue)
    g.plot_pixel(4, 5, Black)

    g.make_image().save("near_random.png")


#   ----- Course -----


    g = Grid(cell_nb = 7, cell_size = 400)

    #g.plot_horizontal_line((0, 0), (6, 0), Black)
    g.plot_vertical_line((6, 0), (6, 6), Green)
    #g.plot_horizontal_line((0, 6), (6, 6), Blue)
    g.plot_vertical_line((0, 0), (0, 6), Green)

    g.plot_horizontal_line((1, 1), (5, 1), Red)
    g.plot_horizontal_line((1, 5), (5, 5), Red)

    g.plot_vertical_line((5, 2), (5, 5), Blue)
    g.plot_vertical_line((1, 1), (1, 4), Blue)


    g.plot_vertical_line((2, 2), (2, 4), Green)
    g.plot_vertical_line((4, 2), (4, 4), Green)

    g.plot_horizontal_line((2, 2), (3, 2), Black)
    g.plot_horizontal_line((3, 4), (4, 4), Black)


    
    g.make_image().save("course_set.png")


    g = Grid(cell_nb = 7, cell_size = 400)

    color_cnt = 0

    for rnd_pixel in range(48):
        x = random.randint(0, 6)
        y = random.randint(0, 6)
        #while(g.color_matrix[y, x, :].tolist() == White): 
        #    x = random.randint(0, 5)
        #    y = random.randint(0, 5)
        g.plot_pixel(x, y, Colors[color_cnt])
        color_cnt = color_cnt + 1 if (color_cnt < 3) else 0

    g.make_image().save("course_random.png")


