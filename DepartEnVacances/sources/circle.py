import math
import random

SCALE = 500
UPPER_CIRCLES_R = 410
LOWER_CIRCLES_R = 410 * .7
COLORS = ['aliceblue', 'brown', 'aquamarine', 'chocolate', 'darkturquoise', 'darkolivegreen', 'gold', 'dimgrey', 'deeppink', 'lime', 'peru', 'orchid']
COLORS2 = COLORS[:]
random.shuffle(COLORS2)
SMALL_CIRCLES_R = 28
STROKE_WIDTH = 5

OFFSET = True


def generate_circle(r, colors, offset=False):
    n_colors = len(colors)
    ws = ""

    for k in range(1, n_colors + 1):
        ws += f"""
            <circle cx="{SCALE + 2 * int(offset) * SCALE + r * math.cos(k * 2 * math.pi / n_colors)}" cy="{SCALE + r * math.sin(k * 2 * math.pi / n_colors)}" r="{SMALL_CIRCLES_R}"
             fill="{colors[k - 1]}" stroke="grey" stroke-width="{STROKE_WIDTH * 0.75}"/>"""

    return ws

def main():
    n_colors = len(COLORS)

    ws = f"""<?xml version="1.0" standalone="no"?>
            <svg width="{2 * SCALE}" height="{2 * SCALE}" viewBox="0 0 {4 * SCALE} {2 * SCALE}"
                 xmlns="http://www.w3.org/2000/svg" version="1.1">
            <desc>Disque de dechiffrage</desc>"""

    ws += f"""<circle cx="{SCALE}" cy="{SCALE}" r="{SCALE * .95}"
             fill="none" stroke="dimgrey" stroke-width="{STROKE_WIDTH}"/>"""

    ws += f"""<circle cx="{SCALE}" cy="{SCALE}" r="7"
             fill="dimgrey" stroke="dimgrey" stroke-width="{STROKE_WIDTH}"/>"""

    ws += generate_circle(UPPER_CIRCLES_R, COLORS)

    # Génération du petit cercle
    ws += f"""<circle cx="{SCALE + 2 * int(OFFSET) * SCALE}" cy="{SCALE}" r="{SCALE * .7}"
                 fill="none" stroke="dimgrey" stroke-width="{STROKE_WIDTH}"/>"""

    ws += generate_circle(LOWER_CIRCLES_R, COLORS2, offset=True)
    ws += f"""<circle cx="{SCALE + 2 * int(OFFSET) * SCALE}" cy="{SCALE}" r="7"
                 fill="dimgrey" stroke="dimgrey" stroke-width="{STROKE_WIDTH}"/>"""

    ws += "</svg>"

    file = open("disque_dechiffrage.svg", "w+")
    file.write(ws)
    file.close()


main()
