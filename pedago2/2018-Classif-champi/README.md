Elle est distribuée sous licence CC-BY.

But : découvrir les arbres de classifications !

Matériel : des images de champignons générés automatiquement.

# Exercice 1 : "trouver des caractéristiques pour faire des classes"
## Déroulé
- On présente 20 images et on leur demande de trouver les caractériques qui font que un champignon est aimé par les escargots (petite emote escargot)
- On demande à chacun ce qu'il a fait, et on introduit la notion d'arbre pour faire les décision
## Objectif
Introduire la notion de feature extraction, et d'un outil de classification: l'arbre de classification.

# Exercice 2 : "utiliser la structure d'arbre"
## Déroulé
- On présente 25 images et on leur demande de faire un arbre de classification. De manière à savoir quelles sont les caractéristiques discriminatives pour que un champignon soit aimé par les vaches (qui a un arbre plus compliqué).
- On demande à chacun ce qu'il a fait, et on fait la remarque que cela permet aussi d'essayer de devner pour des images de champignons que on a pas encore vu.
## Objectif
Introduire la notion de généralisation d'une classif.

# Exercice 3 : "feature extraction"
## Déroulé
- On présente 30 images et on leur demande de de faire un arbre de classification. De manière à savoir quelles sont les caractéristiques discriminatives pour que un champignon soit mortel pour les humains (qui a un arbre plus compliqué). 
- On demande à chacun ce qu'il a fait, et on introduit les notions de précision de la classification en testant sur 10 images qui ne sont pas dans le jeu de données de base de manière à evaluer les scores. On introduit la différence entre faux positif et faux négatif et on fait la remarque que il vaut mieux ne pas en manger que de manger un truc sans être sûr. Moralité, mangez pas sans savoir. On peut si on a le temps parler du rasoir d'Occam.
## Objectif
Conclure et ouvrir


Ps: pour générer les champis:
$ python3 champi/champigen_imag.py
pour info voici le code des arbres.

def loved_by_cow(color, hat, foot, dot):
    if foot == 'inverted':
        return color != 'blue'
    elif foot == 'double':
        return hat == 'bell' or hat == 'conical'
    elif foot == 'without':
        return 'dot' not in dot

def death_for_humans(color, hat, foot, dot):
    if color == 'green':
        return 'dot' in dot
    elif color == 'red':
        if hat == 'bell':
            return True
        elif hat == 'convex':
            return False
        elif hat == 'conical' and 'dot' in dot:
            return True
        elif hat == 'flat' and 'dot' not in dot:
            return True
        else:
            return False
    elif color == 'blue':
        return foot != 'double'

def loved_by_bird(color, hat, foot, dot):
    if hat == 'bell':
        return foot != 'double'
    elif hat == 'convex':
        return color == 'green'
    elif hat == 'conical':
        return foot != 'without'
    elif hat == 'flat':
        return color != 'blue'

def loved_by_snail(color, hat, foot, dot):
    if color == 'green':
        return True
    elif color == 'blue' and 'dot' not in dot:
        return True
    else:
        return False