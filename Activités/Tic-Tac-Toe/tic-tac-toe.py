"""
Jeu «Tic-Tac-Toe» pour la semaine Informatique tous âges.


Auteur: Fermion & Bérillium
"""

# VARIABLES GLOBALES
SYMBOLES = ["X", "O"]   # Symboles possibles
JOUEUR_1 = input("Joueur 1, quel est votre nom? ")  # Nom du joueur 1
JOUEUR_2 = input("Joueur 1, quel est votre nom? ")  # Nom du joueur 2
JOUEURS = [JOUEUR_1, JOUEUR_2]
QUI_JOUE = False    # Joueur qui joue (False == 0; True == 1)

# DÉFINITIONS DES FONCTIONS
def affiche_grille(grille):
    """Affiche la grille (liste) fournie en argument
    
    Args:
        grille (list): Grille de jeu (3x3)
    """

    print("    0   1   2  ")
    print("  *---*---*---*")
    # Boucle pour afficher les éléments de la grille
    for i in range(3):
        # Affiche la ie rangée
        print(i,"| {} | {} | {} |".format(grille[3*i], grille[i*3 + 1], grille[i*3 + 2]))
        print("  *---*---*---*")
    # Fin de la fonction
    return

def choix_joueur(grille):
    """Obtient la case ou le joueur veut jouer.
    
    Args:
        grille (list): Grille de jeu (3x3)
    """
    # Boucle infinie
    while True:
        # Affihce la grille de jeu
        affiche_grille(grille)
        # Demande au joueur où il veut jouer
        print("{} où voulez-vous joueur?".format(JOUEURS[QUI_JOUE]))
        print("Entrez l'indice de la rangé espace de celle de la colone. Exemple: 0 1.\n")

        # Sépare le input aux espacements
        choix = input().split()

        # Vérifie si le input n'est pas composé de 2 éléments
        if len(choix) != 2:
            print("Votre choix doit être de la forme suivante: i j")
            print("'i' est le numéro de la rangé et 'j' celle de la colonne.\n")
        # Sinon, poursuit la procédure
        else:
            # Obtient la rangé/colonne
            row, col = choix[0], choix[1]
            # Essaie de convertir en 'int'
            try:
                row, col = int(row), int(col)
                # Obtient l'indice associé à row et col
                indice = 3 * row + col
                # Vérifie si les nombres entrés sont valides
                if (row < 0 or 2 < row) or (col < 0 or 2 < col):
                    print("Vous devez entrer des chiffres entre 0 et 2.")
                # Vérifie si la case est libre
                elif (grille[indice] != '?'):
                    print("La case choisie n'est pas libre!")
                # Sinon, retourne le choix du joueur
                else:
                    return indice
            # Exception
            except ValueError:
                print("Vous devez entrer des nombres!")

def gagnant(grille):
    """Détermine si le joueur présent a gagné la partie.
    
    Args:
        grille (list): Grille de jeu
    """
    # Obtient la chaine gagnanate
    chaine = SYMBOLES[QUI_JOUE] * 3
    # Combinaisons gagnantes possibles
    combinaisons = [ [0 ,1, 2],[3, 4, 5],[6, 7, 8],
                    [0, 3, 6],[1, 4, 7],[2, 5, 8],
                    [0, 4, 8],[2, 4, 6]]
    # Boucle sur les combinaisons gagnantes
    for comb in combinaisons:
        # Vérifie si une combinaison est gagnante
        if chaine == grille[comb[0]] + grille[comb[1]] + grille[comb[2]]:
            return True
    # Sinon, n'est pas encore gagnant
    return False

# Grille de jeu; initialement vide
grille = ["?", "?", "?", "?", "?", "?", "?", "?", "?"]

# Boucle de jeu
while True:
    # Obtient le choix du joueur
    indice = choix_joueur(grille)
    # Place le symbole du joueur à la position désirée
    grille[indice] = SYMBOLES[QUI_JOUE]

    # Vérifie si le joueur a gagné
    if gagnant(grille):
        print("{} a gagné la partie! Félication!".format(JOUEURS[QUI_JOUE]))
        break
    QUI_JOUE = not QUI_JOUE 