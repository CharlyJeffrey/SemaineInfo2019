"""
Jeu «Tic-Tac-Toe» pour la semaine Informatique tous âges.


Auteur: Fermion & Bérillium
"""

import random as rd

# VARIABLES GLOBALES
COULEURS = ["rouge", "bleu", "vert", "jaune", "violet"]
LONGUEUR_CODE = 4
ESSAIE_MAX = 10

def cree_code():
    """Crée le code de couleurs aléatoire
    """
    code = [None] * LONGUEUR_CODE
    # Boucle pour remplir le code
    for i in range(LONGUEUR_CODE):
        # Ajoute une couleur aléatoire
        code[i] = COULEURS[rd.randint(0, (len(COULEURS)-1))]
    # Retourne le code
    return code

def code_joueur():
    """Obtient le code du joueur
    """
    # Initialise une liste vide
    code = [None] * LONGUEUR_CODE

    # Affiche les couleurs possibles
    msg = ""
    for c in COULEURS:
        msg += " - " + c
    msg += " - "
    print("Couleurs possibles:\n", msg)

    #TODO: Affiche un message pour préciser le nombre de couleurs à choisir
    #...

    # Boucle pour déterminer le choix du joueur
    # Initialise un compteur
    i = 0
    #TODO: Bonne condition pour la boucle
    while (False):
        # Obtient une couleur auprès du joueur
        couleur = input("//>   ")
        
        # Vérifie si la couleur est valide
        #TODO: Bonne condition pour le if
        if False:
            #TOD: Completer le statement
            pass    # <-- À effacer apres!
        else:
            # Message pour couleur invalide
            print("\nChoississez une couleur valide!\n")
    return code

def verfication(codeJoueur, codeOrdi):
    """Vérifie si 'codeJoeurs' et 'codeOrdi' sont identiques
    
    Args:
        codeJoueur (list): Code du joueurs
        codeOrdi (list): Code à deviner
    
    Return:
        Vrai si 'codeJoueur' = 'codeOrdi'
        Faux sinon
    """
    # Initialise des compteurs
    bonEmplacement = 0  # Bonne couleur + bon emplacement
    bonneCouleur = 0    # Bonne couleur, mauvais emplacement

    # Position non-vérifiée
    ordiDispo = [True] * LONGUEUR_CODE
    joueurDispo= [True] * LONGUEUR_CODE

    # On vérifie d'abord bonne couleur + bon emplacement
    for i in range(LONGUEUR_CODE):
        # Vérfie si les couleurs sont identiques
        #TODO: Bonne condition pour le 'if'
        # ...
        if False:
            bonEmplacement += 1     # Augmente le compteur
            ordiDispo[i] = False    # Case vérifiée
            #TODO: Completer le statement
            # ...
    
    # On vérifie ensuite bonne couleur, mauvais emplacement
    for i in range(LONGUEUR_CODE):
        for j in range(LONGUEUR_CODE):
            #TODO: Bonne condition pour le statement
            if (False):
                bonneCouleur += 1
                joueurDispo[i] = False
                ordiDispo[j] = False 
                break
    
    #TODO: Afficher le score associé au choix du joueur
    # ...
    #TODO: Retourner si le choix du joueur est le bon
    return #...


# JEU
print("Bienvenue au jeu MasterMind!\n")
jouer = True
gagner = False

# Boucle de jeu principale
while(jouer):
    # Crée un code à deviner
    codeOrdi = cree_code()
    print("Mon code secret est choisi!")
    #TODO: Afficher le nombre d'essaies que le joueur a
    
    
    # Boucle sur le nombre d'essaie
    essaie = 0
    while essaie < ESSAIE_MAX:
        #TODO: Afficher le nombre d'essaies restant
        # ...
        # Obtient le choix du joueur
        codeJoueur = code_joueur()
        # Vérifie si le joueur a gagné
        gagner = verfication(codeJoueur, codeOrdi)
        #TODO: Vérifier si le joueur a gagné pour arreter la partie
        # ...
        essaie += 1
    
    # Vérifie si le joueur a perdu
    if (gagner == False):
        print("Tu as perdu la partie :(\n")
    
    # Demande au joueur s'il veut rejouer
    rejouer = input("\nVoulez-vous rejouer une autre partie? (Oui ou Non)")
    #TODO: Rejouer une partie si le joueur veut rejouer. Sinon arrêter le jeu.
    # ...
