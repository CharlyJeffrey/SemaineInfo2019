"""
Jeu «Tic-Tac-Toe» pour la semaine Informatique tous âges.


Auteur: Fermion & Bérillium
"""

# Contient les symboles
symboles = ["X", "O"]

# Obtient le nom des joueurs
P1 = input("Joueur 1, quel est votre nom? ")
P2 = input("Joueur 2, quel est votre nom? ")

# Tableau pour contenir le nom des joueurs
joueurs = [P1, P2]

# Variable "switch" pour déterminer qui joue (False == joueur 1; True == joueur 2)
quiJoue = False

def affiche_grille(grid):
    """
    Fonction pour afficher la grille de jeu
    """
    print("    0   1   2  ")
    print("  *---*---*---*")
    for i in range(3):
        print(i,"| {} | {} | {} |".format(grid[i*3], grid[i*3 + 1], grid[i*3 + 2]))
        print("  *---*---*---*")
    return

def choixJoueur(grid):
    """
    Fonction pour obtenir la case où le joueur veut jouer son coup
    """
    while True:
        affiche_grille(grid)
        print("{} où voulez-vous joueur?".format(joueurs[quiJoue]))
        print("Entrez l'indice de la rangé espace de celle de la colone. Exemple: 0 1.\n")

        # Sépare le input aux espacements
        choix = input().split()

        # Vérifie si le input séparé n'est pas composé de 2 termes
        if len(choix) != 2:
            print("Votre choix doit être de la forme suivante: i j")
            print("'i' est le numéro de la rangé et 'j' celle de la colonne.\n")
        
        else:
            # Obtient la rangé/colonne
            row, col = choix[0], choix[1]
            # Essaie de convertir le input en 'int'
            try:
                row, col = int(row), int(col)
                # Obtient la position dans le tableau
                index = 3*row + col
                # Vérifie si les nombres entrés sont valides
                if (row < 0 or 2 < row) or (col < 0 or 2 < col):
                    print("Vous devez entrer des chiffres entre 0 et 2 inclusivement!\n")
                # Vérifie si la case est vide
                elif (grid[index] != "?"):
                    print("La case que vous avez choisie a déjà été prise!!!\n")
                else:
                    return index
            except ValueError:
                print("Vous devez entrer des chiffres!!")

def gagnant(grille):
    """
    Fonction pour déterminer si un joueur a gagné.
    """
    _w = symboles[quiJoue] * 3
    # Arrangements gagnants possibles
    winning = [ [0 ,1, 2],
                [3, 4, 5],
                [6, 7, 8],
                [0, 3, 6],
                [1, 4, 7],
                [2, 5, 8],
                [0, 4, 8],
                [2, 4, 6]]
    
    # Boucle sur les arrangements gagnants
    for cout in winning:
        # Vérifie si une combinaison gagnante se trouve dans la grille
        if _w == grille[cout[0]] + grille[cout[1]] + grille[cout[2]]:
            return True
    return False




# Contient les choix des joueurs; Initialement vide
grille = ["?", "?", "?", "?", "?", "?", "?", "?", "?"]



while True:
    ind = choixJoueur(grille)

    grille[ind] = symboles[quiJoue]

    # Vérifie si un joueur gagne
    if gagnant(grille):
        print("{} a gagné la partie! Félication!".format(joueurs[quiJoue]))
        break
    quiJoue = not quiJoue