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

matrice = [[0 for j in range(COLONNES + 2)] for i in range(RANGEES + 2)]


for i in range(RANGEES):
    for j in range(COLONNES):
        matrice[i+1][j+1] = plateau[i][j]

# nombre de mines autour d'une case
for i in range(1, RANGEES+1):
    for j in range(1, COLONNES+1):
        if matrice[i][j] != 9:
            nb_autour = 0
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if matrice[i+di][j+dj] == 9:
                        nb_autour += 1
            matrice[i][j] = nb_autour

symbol=['0','1','2','3','4','5','6','7','8','X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
ligne=0


for x in range(1,11):
    for b in range(1,11):
        matrice[x][b]+=10

def affichage():
    ligne=0
    print("  1   2   3   4   5   6   7   8   9  10")
    print("+---+---+---+---+---+---+---+---+---+---+")
    for i in range(1,11):
        ligne+=1
        print("|",symbol[matrice[ligne][1]], "|", symbol[matrice[ligne][2]], "|", symbol[matrice[ligne][3]],"|",symbol[matrice[ligne][4]], "|", symbol[matrice[ligne][5]], "|", symbol[matrice[ligne][6]],"|",symbol[matrice[ligne][7]], "|", symbol[matrice[ligne][8]], "|", symbol[matrice[ligne][9]],"|",symbol[matrice[ligne][10]],"|",ligne)
        print("+---+---+---+---+---+---+---+---+---+---+")
def tour():
    affichage()
    decouverte()
    tour()

def decouverte():
    coordX = int(input('Entrer la position X de votre sélection'))
    if 0<coordX<11:
        coordY = int(input('Entrer la position Y de votre sélection'))
        if 0<coordY<11:
            if matrice[coordY][coordX]>9:
                matrice[coordY][coordX]-=10
                if matrice[coordY][coordX] == 9:
                    perdu()
                    quit()
            else: tour()
        else: tour()
    else: tour()

def perdu():
    print('Vous avez perdu !')
    for x1 in range(1, 11):
        for b1 in range(1, 11):
            if matrice[x1][b1] == 19:
                matrice[x1][b1]-=10
    affichage()
    quit()
tour()

