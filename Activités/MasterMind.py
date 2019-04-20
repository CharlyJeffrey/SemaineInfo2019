import random

# Longueur du code caché
NBR_COULEUR = 4

#couleur possible
couleur = ["rouge", "bleu", "violet", "vert", "jaune"] # Possibilite d'ajouter plus de couleurs

#fonction pour creer le code de couleur de base
def creerCode():
    codeBase = [None]*NBR_COULEUR
    for x in range (0,NBR_COULEUR):
        codeBase[x] = couleur [random.randint(0,(len(couleur)-1))]
    return codeBase

#verification code
def verifierCode(codeJoueur, codeOrdi):
    bonEmplacementOuCouleur = [0,0]
    ordiDisponible  = [True, True, True, True] #pour savoir si on en prend deja compte
    joueurDisponible  = [True, True, True, True] #pour savoir si on en prend deja compte
    #on commence par le meme endroit, la priorite
    for x in range (0,NBR_COULEUR):
        if(codeJoueur[x] == codeOrdi[x]):
            bonEmplacementOuCouleur[0] += 1 #bonne couleur au bon endroit
            ordiDisponible[x] = False
            joueurDisponible[x] = False

    #on poursuit avec la meme couleur pas le meme endroit
    for x in range (0,NBR_COULEUR):
        for y in range (0,NBR_COULEUR):
            if(codeJoueur[x] == codeOrdi[y]):
                if (ordiDisponible[y] & joueurDisponible[x]):
                    bonEmplacementOuCouleur[1] += 1 #bonne couleur au mauvais endroit
                    ordiDisponible[y] = False
                    joueurDisponible[x] = False
                    break
    #savoir si le jeu est termine
    if bonEmplacementOuCouleur[0] == NBR_COULEUR:
        print("Wow, tu m'as battu!")
        return True
    #savoir ce qui est bon ou pas
    else:
        print("Vous avez", bonEmplacementOuCouleur[0], "pion(s) ayant la bonne couleur au bon endroit"\
            "\nVous avez aussi", bonEmplacementOuCouleur[1], "pion(s) ayant la bonne couleur mais" \
            " au mauvais endroit \n")
        return False


#code python: masterMind


#Banque de test
#codejeu = ["bleu", "jaune", "bleu", "bleu"]
#codeOrdi = creerCode()
#print(codeOrdi[0], codeOrdi[1], codeOrdi[2], codeOrdi[3], len(codeOrdi))
#codeOrdi = ["bleu", "bleu", "rouge", "rouge"]
#verifierCode(codejeu, codeOrdi)
print ("Bienvenue au jeu de MasterMind!\n")
jouer = True
deviner = False
while(jouer):
    codeOrdi = creerCode()
    choixJoueur = [None]*NBR_COULEUR
    print("J'ai mon code, tu as 10 essais pour le deviner!")
    print(codeOrdi)
    for x in range(0,10):

        i = 0
        while (i < NBR_COULEUR):
            _choix = input("\nEntrez une couleur: rouge, bleu, violet, vert ou jaune: ")
            if _choix not in couleur:
                print("\nCouleur invalide! Refaite votre choix\n")
            else :
                choixJoueur[i] = _choix
                i += 1
        
        deviner = verifierCode(choixJoueur, codeOrdi)
        if (deviner):
            print("\nBravo tu m'as vaincu!")
            break
            
    if (deviner == False):
        print("\nJe suis trop fort pour toi gros loser!")
    rejouer = input("\nOn rejoue? ")
    if (rejouer == "non"):
        jouer = False
        print("\nok bye! ")