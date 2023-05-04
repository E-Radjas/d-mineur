import random as rd

MINES = [rd.randint(0, 9)]
NB_MINES = 10
rangees = 10
COLONNES = 10
plateau = [[0 for j in range(COLONNES)] for i in range(rangees)]

for i in range(NB_MINES):
    row = rd.randint(0, rangees - 1)
    col = rd.randint(0, COLONNES - 1)
    while plateau[row][col] == 9:
        row = rd.randint(0, rangees - 1)
        col = rd.randint(0, COLONNES - 1)
    plateau[row][col] = 9

# Affichage du cadre
matrice = [[11 for j in range(COLONNES + 2)] for i in range(rangees + 2)]


for i in range(rangees):
    for j in range(COLONNES):
        matrice[i+1][j+1] = plateau[i][j]

# nombre de mines autour d'une case
for i in range(1, rangees + 1):
    for j in range(1, COLONNES+1):
        if matrice[i][j] != 9:
            nb_autour = 0
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if matrice[i+di][j+dj] == 9:
                        nb_autour += 1
            matrice[i][j] = nb_autour

for ligne in matrice:
    print(ligne)
