import random as rd

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
for i in range(row):
    if i + 1 == 9 or 1 - 1 == 9:
        i += 1
for i in range(col):
    if i + 1 == 9 or 1 - 1 == 9:
        i += 1
matrice = [[0 for j in range(COLONNES + 2)] for i in range(RANGEES + 2)]
print(plateau)
