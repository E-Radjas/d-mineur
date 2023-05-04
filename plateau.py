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




import random

continuer=1
# Fonction pour initialiser le plateau de jeu
while continuer==1:
    def initialiser_plateau(largeur, hauteur, nb_mines):
        plateau = [[0 for j in range(largeur)] for i in range(hauteur)]
        mines_placees = 0
        while mines_placees < nb_mines:
            x = random.randint(0, largeur - 1)
            y = random.randint(0, hauteur - 1)
            if plateau[y][x] != 'X':
                plateau[y][x] = 'X'
                mines_placees += 1
                for i in range(max(0, y-1), min(hauteur, y+2)):
                    for j in range(max(0, x-1), min(largeur, x+2)):
                        if plateau[i][j] != 'X':
                            plateau[i][j] += 1
        return plateau

# Fonction pour afficher le plateau de jeu
    def afficher_plateau(plateau, decouvert):
        print('  ' + ' '.join(str(i) for i in range(len(plateau[0]))))
        for i in range(len(plateau)):
            ligne = ''
            for j in range(len(plateau[0])):
                if decouvert[i][j]:
                    ligne += str(plateau[i][j])
                else:
                    ligne += '-'
            print(str(i) + ' ' + ligne)

# Fonction pour révéler une case
    def reveler_case(plateau, decouvert, x, y):
        if decouvert[y][x]:
            return decouvert[y][x]==True
        if plateau[y][x] == 'X':
            return False
        if plateau[y][x] == 0:
            for i in range(max(0, y-1), min(len(plateau), y+2)):
                for j in range(max(0, x-1), min(len(plateau[0]), x+2)):
                    reveler_case(plateau, decouvert, j, i)
            return True

# Fonction pour demander des coordonnées
    def demander_coordonnees():
        while True:
            coordonnees = input('Entrez les coordonnées (x,y) ou q pour quitter : ')
            if coordonnees.lower() == 'q':
                return None
            try:
                x, y = [int(c) for c in coordonnees.split(',')]
                if x < 0 or x >= 10 or y < 0 or y >= 10:
                    print('Coordonnées invalides.')
                else:
                    return x, y
            except:
                print('Coordonnées invalides.')

# Fonction principale pour jouer au démineur
    def jouer_demineur():
        nb_mines = 10
        plateau = initialiser_plateau(10, 10, nb_mines)
        decouvert = [[False for j in range(10)] for i in range(10)]
        partie_terminee = False
        while not partie_terminee:
            afficher_plateau(plateau, decouvert)
            coordonnees = demander_coordonnees()
            if coordonnees is None:
                print('Au revoir!')
                return x,y==coordonnees
            if not reveler_case(plateau, decouvert, x, y):
                print('BOUM ! Vous avez perdu')
