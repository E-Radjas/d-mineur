import random as rd

MINES = [rd.randint(0, 9)]
NB_MINES = 10
RANGEES = 10
COLONNES = 10
matrice = [[0 for j in range(COLONNES)] for i in range(RANGEES)]
## matrice = [[0,0,0,0,0,0,0,0,0,0],
##           [0,0,0,0,0,0,0,0,0,0],
##           [0,0,0,0,0,0,0,0,0,0],
##           [0,0,0,0,0,0,0,0,0,0],
##           [0,0,0,0,0,0,0,0,0,0],
##           [0,0,0,0,0,0,0,0,0,0],
##           [0,0,0,0,0,0,0,0,0,0],
##           [0,0,0,0,0,0,0,0,0,0],
##           [0,0,0,0,0,0,0,0,0,0]]

for i in range(NB_MINES):
    row = rd.randint(0, RANGEES - 1)
    col = rd.randint(0, COLONNES - 1)
    while matrice[row][col] == 9:
        row = rd.randint(0, RANGEES - 1)
        col = rd.randint(0, COLONNES - 1)
    matrice[row][col] = 9

print(matrice)
