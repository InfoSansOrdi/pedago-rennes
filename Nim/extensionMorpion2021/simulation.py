import numpy as np
import random

"""
Cette fonction cherche dans le tableau de jeu s'il existe une ligne/colonne/diagonale avec une seule case à compléter pour déclenrcher une victoire.
@param board tableau de jeu sous la forme d'un numpy 3x3 composée de 0 (case vide), 1 (croix) et -1 (rond)
@param target la valeur entrée doit être 2 pour chercher une victoire de la croi, -2 pour une victoire du rond.
@Return un triplet (bool, int, int) indiquant la présence d'une victoire potentielle et les coordonnées de la case à compléter pour déclencher la victoire
"""
def searchPotentialWin(board, target):
    col = np.sum(board, axis=0)
    line = np.sum(board, axis=1)
    #print(col, line)
    for i in range(3):
        if (col[i] == target):
            for j in range(3):
                if (board[j][i] == 0):
                    return (True, j, i)
    for i in range(3):
        if (line[i] == target):
            for j in range(3):
                if (board[i][j] == 0):
                    return (True, i, j)
    if (sum([board[i][i] for i in range(3)]) == target):
        for i in range(3):
            if (board[i][i] == 0):
                    return (True, i, i)
    if (board[0,2]+board[2,0]+board[1,1]) == target:
        for i, j in [(0,2), (2,0), (1,1)]:
            if (board[i][j] == 0):
                    return (True, i, j)
    return (False, 0, 0)

"""
Cherche une ligne/colonne/diagonale complète sur le board avec que des croix ou que des ronds (victoire du rond ou de la croix)
@param board tableau de jeu sous la forme d'un numpy 3x3 composée de 0 (case vide), 1 (croix) et -1 (rond)
@return 0 si pas de vcitoire, 1 pour une victoire de la croix et -1 pour une victoire du rond
"""
def hasWin(board):
    col = np.sum(board, axis=0)
    line = np.sum(board, axis=1)
    for i in range(3):
        if (col[i] == 3):
            return 1
        if (col[i] == -3):
            return -1
    for i in range(3):
        if (line[i] == 3):
            return 1
        if (line[i] == -3):
            return -1
    if (sum([board[i][i] for i in range(3)]) == 3):
        return 1
    if (sum([board[i][i] for i in range(3)]) == -3):
        return -1
    if (board[0,2]+board[2,0]+board[1,1]) == 3:
        return 1
    if (board[0,2]+board[2,0]+board[1,1]) == -3:
        return -1
    return 0

#Détermine si la partie est terminée (vctoire d'un des joueurs) et donne le gagnant.
def isEnd(board):
    result = hasWin(board)
    return ((result != 0), result)

"""
Simulation du tour de l'utilisateur (le choix de la case à jouer est fait au hasard)
@param board tableau de jeu sous la forme d'un numpy 3x3 composée de 0 (case vide), 1 (croix) et -1 (rond)
@return un doublet (i, j) donnant les coordonnées de la case choisie pour jouer.
"""
def randomTurn(board):
    possibleWin, i, j = searchPotentialWin(board, 2)
    if (possibleWin):
        return (i, j)
    else:
        [i, j] = np.random.choice(3, 2)
        while (board[i][j] != 0):
            [i, j] = np.random.choice(3, 2)
        return (i, j)

"""
Simulation du tour de l'IA
@param board tableau de jeu sous la forme d'un numpy 3x3 composée de 0 (case vide), 1 (croix) et -1 (rond)
@param un tableau de 4 tableaux représentant les jetons contenues dans les gobelets.
@return un doublet (i, j) donnant les coordonnées de la case choisie pour jouer.
"""
def iaTurn(board, gobelet):
    possibleWin, i, j = searchPotentialWin(board, -2)
    if (possibleWin):
        return (i, j)
    while (len(gobelet) == 0):
        choice = random.choice(gobelet)
        gobelet.remove(choice)
        if choice == 'centre' and board[1][1] == 0:
            return (1, 1)
        elif choice == 'coin' and (board[0][0] == 0 or board[0][2] == 0 or board[2][0] == 0 or board[2][2] == 0):
            if board[0][0] == 0:
                return 0, 0
            elif board[2][0] == 0:
                return 2, 0
            elif board[0][2] == 0:
                return 0, 2
            else:
                return 2, 2
        elif choice == 'bord' and (board[0][1] == 0 or board[1][2] == 0 or board[2][1] == 0 or board[1][0] == 0):
            if board[0][1] == 0:
                return 0, 1
            elif board[2][1] == 0:
                return 2, 1
            elif board[1][2] == 0:
                return 1, 2
            else:
                return 1, 0 
        

#Fonction de simulation d'une partie avec n tour, TODO : à terminer
def simu(n):
    gobelets = [['coin', 'bord', 'centre'], ['coin', 'bord', 'centre'], ['coin', 'bord', 'centre'], ['coin', 'bord', 'centre']]
    for i in range(n):
        end = False
        winner = "Erreur"
        k = 0
        lastModified = ''
        while (not(end)):
            board = np.zeros(3,3)
            lastMosdified, i, j = iaTurn(board, gobelets[k])
            board[i][j] = -1
            i, j = randomTurn(board)
            end, winner = isEnd(board)
            k += 1
        gobeletsiaLearn(gobelets, k)
        print(winner)

board = np.array([ [-1, -1, -1],
                   [0, 0, 0],
                   [-1, 1, -1]])
#print(hasWin(board))