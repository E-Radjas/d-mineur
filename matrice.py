import random as rd
import time

import pygame as pg

# Initialisation pygame
pg.init()


def reveler_cases_adjacentes(row, col):
    """
    Révèle récursivement les cases adjacentes vides.
    """
    global matrice
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if matrice[row + di][col + dj] > 9:
                matrice[row + di][col + dj] -= 10
                if matrice[row + di][col + dj] == 0:
                    reveler_cases_adjacentes(row + di, col + dj)


def découverte(coordX, coordY):
    """
    Gère la découverte d'une case par le joueur.
    """
    global matrice, game_over
    if 0 < coordX < 11 and 0 < coordY < 11:
        if 20 > matrice[coordY][coordX] > 9:
            matrice[coordY][coordX] -= 10
            if matrice[coordY][coordX] == 9:
                game_over = True
            if matrice[coordY][coordX] == 0:
                reveler_cases_adjacentes(coordY, coordX)


def flag(coordX, coordY):
    """
    Place ou retire un drapeau sur une case.
    """
    global matrice
    if 0 < coordX < 11 and 0 < coordY < 11:
        if 20 > matrice[coordY][coordX] > 9:
            matrice[coordY][coordX] += 10
        elif matrice[coordY][coordX] >= 20:
            matrice[coordY][coordX] -= 10


def verifier_victoire():
    """
    Vérifie si le joueur a gagné en découvrant toutes les cases sans mine.
    """
    global matrice, game_over
    mines_restantes = sum(1 for ligne in matrice for case in ligne if case == 9)
    if mines_restantes == NB_MINES:
        game_over = True


def afficher_perdu():
    """
    Affiche toutes les mines pendant quelques secondes lorsque le joueur perd.
    """
    global matrice
    for l in range(1, len(matrice) - 1):
        for c in range(1, len(matrice[0]) - 1):
            if matrice[l][c] == 9:
                matrice[l][c] -= 10  # Révèle la mine
    time.sleep(3)  # Attendre 3 secondes

    # Est-ce que pygame est initialisé ? (pour quitter)
    if pg.get_init():
        pg.quit()  # Fermer le jeu



# Constantes
MINES = [rd.randint(0, 9)]
NB_MINES = 10
RANGEES = 10
COLONNES = 10

# Initialisation pygame
pg.init()
fenêtre = pg.display.set_mode((640, 640), pg.RESIZABLE)

# Images
case_1 = pg.image.load("tile_1.png").convert_alpha()
case_2 = pg.image.load("tile_2.png").convert_alpha()
case_3 = pg.image.load("tile_3.png").convert_alpha()
case_4 = pg.image.load("tile_4.png").convert_alpha()
case_5 = pg.image.load("tile_5.png").convert_alpha()
case_6 = pg.image.load("tile_6.png").convert_alpha()
case_7 = pg.image.load("tile_7.png").convert_alpha()
case_8 = pg.image.load("tile_8.png").convert_alpha()
case_0 = pg.image.load("tile_clicked.png").convert_alpha()
drapeau = pg.image.load("tile_flag.png").convert_alpha()
mine = pg.image.load("tile_mine.png").convert_alpha()
case_vide = pg.image.load("tile_plain.png").convert_alpha()
list_im = [case_0, case_1, case_2, case_3, case_4, case_5, case_6, case_7, case_8, mine, case_vide, drapeau]

# Mise en place du jeu
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

# Nombre de mines autour de chaque case
for i in range(1, RANGEES + 1):
    for j in range(1, COLONNES + 1):
        if matrice[i][j] != 9:
            nb_autour = 0
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if matrice[i + di][j + dj] == 9:
                        nb_autour += 1
            matrice[i][j] = nb_autour
for i in range(1, RANGEES + 1):
    for j in range(1, COLONNES + 1):
        matrice[i][j] += 10
symbol = ['0', '1', '2', '3', '4', '5', '6', '7', '8', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '►']

# Boucle du jeu
running = True
clic = False
game_over = False  # Variable pour voir l'état du jeu
while running:
    # Evenements pygame
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    if game_over:
        afficher_perdu()

    if pg.mouse.get_pressed()[0]:
        découverte((pg.mouse.get_pos()[0] + 64) // 64, (pg.mouse.get_pos()[1] + 64) // 64)
    if pg.mouse.get_pressed()[2] and not clic:
        flag((pg.mouse.get_pos()[0] + 64) // 64, (pg.mouse.get_pos()[1] + 64) // 64)
        clic = True
    if not pg.mouse.get_pressed()[2]:
        clic = False

    # Regarder si toutes les cases sont des mines
    if not game_over:
        verifier_victoire()

    # Montrer le plateau
    for l in range(1, len(matrice) - 1):
        for c in range(1, len(matrice[0]) - 1):
            if matrice[l][c] < 20:
                fenêtre.blit(list_im[min(matrice[l][c], 10)], (c * 64 - 64, l * 64 - 64))
            else:
                fenêtre.blit(list_im[11], (c * 64 - 64, l * 64 - 64))

    pg.display.flip()
