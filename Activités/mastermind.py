"""
Jeu «Mastermind» pour la semaine Informatique tous âges.


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
    # Initialise un compteur
    i = 0
    # Boucle pour déterminer le choix du joueur
    print("\nCoississez {} couleurs:".format(LONGUEUR_CODE))
    while (i < LONGUEUR_CODE):
        couleur = input("//>   ")
        
        # Vérifie si la couleur est valide
        if couleur in COULEURS:
            code[i] = couleur
            i += 1
        else:
            print("\nChoississez une couleur valide!\n")
    return code

def verfication(codeJoueur, codeOrdi):
    """Vérifie si 'codeJoeurs' et 'codeOrdi' sont identiques
    
    Args:
        codeJoueur (list): Code du joueurs
        codeOrdi (list): Code à deviner
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
        if (codeJoueur[i] == codeOrdi[i]):
            bonEmplacement += 1     # Augmente le compteur
            ordiDispo[i] = False    # Case vérifiée
            joueurDispo[i] = False   # Case vérifiée
    
    # On vérifie ensuite bonne couleur, mauvais emplacement
    for i in range(LONGUEUR_CODE):
        for j in range(LONGUEUR_CODE):
            # Vérifie si les couleurs sont identiques et disponible
            if (codeJoueur[i] == codeOrdi[j] and joueurDispo[i] and ordiDispo[j]):
                bonneCouleur += 1
                joueurDispo[i] = False
                ordiDispo[j] = False 
                break
                
    print("\nBonne couleur et bon emplacement:", bonEmplacement)
    print("Bonne couleur, mauvais endroit:", bonneCouleur)
    print("\n")
    return bonEmplacement == LONGUEUR_CODE


# JEU
print("Bienvenue au jeu MasterMind!\n")
jouer = True
gagner = False

# Boucle de jeu principale
while(jouer):
    # Crée un code à deviner
    codeOrdi = cree_code()
    print("Mon code secret est choisi!")
    print("Vous avez {} essaies pour le deviner! Bonne chance.".format(ESSAIE_MAX))
    
    # Boucle sur le nombre d'essaie
    essaie = 0
    while essaie < ESSAIE_MAX:
        print("Essaie {} de {}.".format(essaie, ESSAIE_MAX))
        # Obtient le choix du joueur
        codeJoueur = code_joueur()
        # Vérifie si le joueur a gagné
        gagner = verfication(codeJoueur, codeOrdi)
        if gagner:
            print("\nBravo tu as gagné!")
            break
        essaie += 1
    
    # Vérifie si le joueur a perdu
    if (gagner == False):
        print("Tu as perdu la partie :(\n")
    
    # Demande au joueur s'il veut rejouer
    rejouer = input("\nVoulez-vous rejouer une autre partie? (Oui ou Non)")
    # Vérifie si le joueur veut rejouer
    if rejouer[0].lower() == 'o':
        print("Ok! On va rejouer!\n\n\n")
    else:
        print("Dommage :(")
        jouer = False