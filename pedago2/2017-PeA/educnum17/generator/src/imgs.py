# WARNING : need python pillow dependency
from PIL import Image, ImageDraw

# Create card image from a card with image path as attributes
# card : dictionary <name, value> of a card
# return: The merging of all attributes in one image
def create_card(card, dir):
    imgcard = None

    for natt in card:
        img = Image.open(dir + card[natt])

        if imgcard == None:
            imgcard = img
        else:
            imgcard.paste(img, (0,0), img)

    h, w = imgcard.size
    l = 1
    color="#000"
    draw = ImageDraw.Draw(imgcard)
    draw.rectangle((0,0, h -l, w -l), outline=color)

    return imgcard

# Create the cards images of list of cards
# cards : list of cards
# return a list of images
def create_card_list(cards, dir):
    limgs = []
    for c in cards:
        limgs.append(create_card(c, dir))
    return limgs
