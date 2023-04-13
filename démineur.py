import pygame as pg
import random as rd
MINES = [rd.randint(0, 9)]
NB_MINES = 10
ROWS = 10
COLS = 10
matrix = [[0 for j in range(COLS)] for i in range(ROWS)]
## matrice = [[0,0,0,0,0,0,0,0,0,0],
##           [0,0,0,0,0,0,0,0,0,0],
##           [0,0,0,0,0,0,0,0,0,0],
##           [0,0,0,0,0,0,0,0,0,0],
##           [0,0,0,0,0,0,0,0,0,0],
##           [0,0,0,0,0,0,0,0,0,0],
##           [0,0,0,0,0,0,0,0,0,0],
##           [0,0,0,0,0,0,0,0,0,0],
##           [0,0,0,0,0,0,0,0,0,0]]

for i in range(NUM_MINES):
    row = rd.randint(0, ROWS - 1)
    col = rd.randint(0, COLS - 1)
    while matrice[row][col] == 9:
        row = rd.randint(0, ROWS - 1)
        col = rd.randint(0, COLS - 1)
    matrice[row][col] = 9
