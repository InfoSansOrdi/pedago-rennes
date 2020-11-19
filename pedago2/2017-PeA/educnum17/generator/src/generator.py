import random
import copy

# attributes sample
attributes = {"a1":[1, 2, 3],
              "a2":[1, 2, 3]}
# Model sample
model={"a1": 3, "a2":2}


# Generate a list of attributes to use for model generation
# attributes: dictionary <name, list of values> of all system attributes
# model: dictionary <name, int> of attributes to generate in the system and the number of values of this attribute
# [seed]: RNG seed
# return: dictionary <name, list of values> of the selected values in the system
def generate_latt(attributes, model, seed=None):
    latt = {}
    random.seed(seed)
    for a in model:
        nbr = model[a]
        attribute = attributes[a]
        selected = random.sample(attribute, nbr)
        latt[a] = selected
    return latt

# Generate a list of cards attributes
# attributes: dictionary <name, list of values> of all system attributes
# model: dictionary <name, int> of attributes to generate in the system and the number of values of this attribute
# [seed]: RNG seed
# return: list of dictionary <name, value> of all possibilities of cards for the model
def generate(attributes, model, seed=None):
    latt = generate_latt(attributes, model, seed)
    cards = []
    ncards = []

    for aname in latt:
        att = latt[aname]
        if len(cards) == 0: # initial state
            for a in att:
                ncards.append({aname:a})
        else:
            for a in att:
                for c in cards:
                    c[aname] = a
                    nc = copy.deepcopy(c)
                    nc[aname] = a
                    ncards.append(nc)
        cards = ncards
        ncards = []
    return cards
