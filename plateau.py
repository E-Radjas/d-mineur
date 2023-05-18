import random as rd
from time import sleep

MINES = [rd.randint(0, 9)]
NB_MINES = 10
RANGEES = 10
COLONNES = 10
plateau = [[0 for j in range(COLONNES)] for i in range(RANGEES)]

for i in range(NB_MINES):
    row = rd.randint(0, RANGEES - 1)
    col = rd.randint(0, COLONNES - 1)
    while plateau[row][col] == 9:
        row = rd.randint(0, RANGEES - 1)
        col = rd.randint(0, COLONNES - 1)
    plateau[row][col] = 9

matrice = [[0 for j in range(COLONNES + 2)] for i in range(RANGEES + 2)]

for i in range(RANGEES):
    for j in range(COLONNES):
        matrice[i + 1][j + 1] = plateau[i][j]

# nombre de mines autour d'une case
for i in range(1, RANGEES + 1):
    for j in range(1, COLONNES + 1):
        if matrice[i][j] != 9:
            nb_autour = 0
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if matrice[i + di][j + dj] == 9:
                        nb_autour += 1
            matrice[i][j] = nb_autour

symbol = ['0', '1', '2', '3', '4', '5', '6', '7', '8', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '►']
ligne = 0

for x in range(1, 11):
    for b in range(1, 11):
        matrice[x][b] += 10


def affichage():
    ligne = 0
    print("  1   2   3   4   5   6   7   8   9  10")
    print("+---+---+---+---+---+---+---+---+---+---+")
    for i in range(1, 11):
        ligne += 1
        print("|", symbol[matrice[ligne][1]], "|", symbol[matrice[ligne][2]], "|", symbol[matrice[ligne][3]], "|",
              symbol[matrice[ligne][4]], "|", symbol[matrice[ligne][5]], "|", symbol[matrice[ligne][6]], "|",
              symbol[matrice[ligne][7]], "|", symbol[matrice[ligne][8]], "|", symbol[matrice[ligne][9]], "|",
              symbol[matrice[ligne][10]], "|", ligne)
        print("+---+---+---+---+---+---+---+---+---+---+")


def tour():
    affichage()
    decouverte()
    tour()


def decouverte():
    try:
        coordX = int(input('Entrer la position X de votre sélection'))
        coordY = int(input('Entrer la position Y de votre sélection'))
    except ValueError:
        decouverte()
        return

    if coordX == 0 or coordY == 0:
        decouverte()
        return

    if 0 < coordX < 11 and 0 < coordY < 11:
        if matrice[coordY][coordX] > 9:
            matrice[coordY][coordX] -= 10
            if matrice[coordY][coordX] == 9:
                perdu()
                quit()
            if matrice[coordY][coordX] == 0:
                reveler_cases_adjacentes(coordY, coordX)
        else:
            tour()
    else:
        tour()


def reveler_cases_adjacentes(row, col):
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if matrice[row + di][col + dj] > 9:
                matrice[row + di][col + dj] -= 10
                if matrice[row + di][col + dj] == 0:
                    reveler_cases_adjacentes(row + di, col + dj)


def perdu():
    for x1 in range(1, 11):
        for b1 in range(1, 11):
            if matrice[x1][b1] == 19:
                matrice[x1][b1] -= 10
    affichage()
    print('Vous avez perdu ! /n Le jeu se fermera dans 10 secondes')
    sleep(10)
    quit()


tour()