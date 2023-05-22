import random as rd
import pygame as pg
def reveler_cases_adjacentes(row, col):
    global matrice
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if matrice[row + di][col + dj] > 9:
                matrice[row + di][col + dj] -= 10
                if matrice[row + di][col + dj] == 0:
                    reveler_cases_adjacentes(row + di, col + dj)
        
def decouverte(coordX, coordY):
    global matrice
    if 0 < coordX < 11 and 0 < coordY < 11:
        if 20>matrice[coordY][coordX] > 9:
            matrice[coordY][coordX] -= 10
            if matrice[coordY][coordX] == 9:
                quit()
            if matrice[coordY][coordX] == 0:
                reveler_cases_adjacentes(coordY, coordX)
def flag(coordX, coordY):
    global matrice
    if 0 < coordX < 11 and 0 < coordY < 11:
        if 20>matrice[coordY][coordX] > 9:
            matrice[coordY][coordX] += 10
        elif matrice[coordY][coordX] >= 20:
            matrice[coordY][coordX] -= 10
# Constantes
MINES = [rd.randint(0, 9)]
NB_MINES = 10
RANGEES = 10
COLONNES = 10

# Pygame initialisation
pg.init()
fenetre = pg.display.set_mode((640, 640), pg.RESIZABLE)

# Load images
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
drapeau = pg.image.load("tile_flag.png").convert_alpha()
list_im=[case_0,case_1,case_2,case_3,case_4,case_5,case_6,case_7,case_8, mine, case_vide, drapeau]

# Game state setup
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

# Number of mines around a cell
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
        matrice[i][j]+=10
symbol = ['0', '1', '2', '3', '4', '5', '6', '7', '8', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '►']

# Game loop
running = True
clic=False
while running:
    # Event handling
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    if pg.mouse.get_pressed()[0]: decouverte((pg.mouse.get_pos()[0]+64) // 64, (pg.mouse.get_pos()[1]+64) // 64)
    if pg.mouse.get_pressed()[2] and clic==False:
        flag((pg.mouse.get_pos()[0]+64) // 64, (pg.mouse.get_pos()[1]+64) // 64)
        clic=True
    if pg.mouse.get_pressed()[2]==False : clic=False
    for l in range(1, len(matrice) - 1):
        for c in range(1, len(matrice[0]) - 1):
            if matrice[l][c]<20:
                fenetre.blit(list_im[min(matrice[l][c], 10)], (c * 64-64, l * 64-64))
            else:fenetre.blit(list_im[11], (c * 64-64, l * 64-64))
                
    pg.display.flip()
