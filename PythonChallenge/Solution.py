"""
Solution des défis python
"""
import datetime

# Obtient la date actuelle (yyyy/mm/dd)
now = str(datetime.datetime.now())

YEAR = int(now[0:4])
MONTH = int(now[5:7])
DAY = int(now[8:10]) 

def testSolution(func, *args):
    """
    Fonction pour tester une certaine fonction donnée en argument.
    Affiche le résultat de la fonction
    """
    if (len(args) < 1):
        format_args = (func.__name__, "", func())
    else :
        format_args = (func.__name__, *args, func(*args))
    print("Utilisation de {}({}): résultat: {}".format(*format_args))
¸

def HelloWorld():
    """
    Fonction d'introduction aux commandes input/print.
    Demande à l'utilisateur son nom, son âge ainsi une chose qu'il aime.
    Affiche ensuite ces information sous la forme d'un message amicale.
    """
    # Demande le nom de la personne
    nom = input("Quel est votre nom? ")
    # Demande l'âge
    age = input("Quel est votre âge? ")
    # Demande une chose que la personne aime
    aime = input("Nommez une chose que vous aimez: ")
    # Affiche un petit message amicale
    return "Bonjour " +nom+ ", vous avez " +age+" ans et vous aimez "+aime

def inverseCaps(mot):
    """
    Fonction pour inverse les majuscules et minuscules d'un certain
    mot donné en argument. 
    """
    # Toutes les lettre en minuscules
    lettres = "abcdefghijklmnopqrstuvwxyz"
    # Initialise le mot qui sera retourné
    mot_inv = ""
    # Boucle sur le mot original
    for l in mot:
        # Vérifie si la lettre (l) est minuscule
        if l in lettres:
            # Ajoute la lettre (l) en majuscule à mot_inv
            mot_inv += l.upper()
        # Sinon la lettre se trouve forcement dans les majuscule
        else:
            # Ajoute la lettre (l) en minuscule à mot_inv
            mot_inv += l.lower()
    # Retourne mot_inv
    return mot_inv

# Solution du probleme
def nombreDeVoyelles(phrase):
    """
    Fonction pour déterminer le nombre de voyelles qu'une phrase fournie
    en input contient.
    """
    # Toutes les voyelles de l'alphabet
    voyelle = "aeiouy"
    # Compteur du nombre de voyelle du mot
    nombre_voyelles = 0
    # boucle sur toutes les caractères de la phrase
    for c in phrase:
        # Vérifie si le caractère est une voyelle
        if c.lower() in voyelle:
            # Augmente le compteur
            nombre_voyelles += 1
    # Retourne compteur
    return nombre_voyelles

# Solution du problème 
def plusLongMot(phrase) :
    """
    Fonction pour déterminer le plus long mot d'une phrase donnée en argument.
    Utilise la méthode built-in «split()».

    Commencez par ignorer la partie qui ignore les caractères qui ne sont
    pas des lettres. Demmandez ensuite aux jeunes de le faire.

    Notions à savoir:
        - Manipulation de string (len,(), .lower())
        - Boucle (for x in tab)
        - Opération logique (if)
    """
    # Initialise un mot vide
    mot = ""
    # Caractère à ignorer (petit bonus)
    carac = "abcdefghijklnopqrstuvwxyz"
    # En utilisant la fonction built-in «split()»
    tableauMots = phrase.split()
    # Boucle sur les éléments (mots)
    for m_ in tableauMots:
        # Boucle sur m pour vérifier et ignorer les caractères spécifiés
        # Initialise un mot vide
        m = ""
        for c in m_:
            # Vérifie si le caractère est une lettre
            if c.lower() in carac:
                # Ajoute le caractère
                m += c
        # Vérifie si la longuer de mot est plus longue
        if len(mot) < len(m):
            mot = m
    return mot

# Solution du probleme 
def somme(n):
    """
    Fonction pour déterminer la somme de tous les entiers entre 1 et n,
    inclusivement. 

    Peut se faire en uitilisant une boucle for ou while.

    Notions à savoir:
        - Opération simple (addition)
        - Boucle (for, while)
    """
    # Initialisation d'une varaible pour stocker la valeur de la somme
    sum = 0
    # Variable d'itération (commence à 1)
    iter = 1
    # Boucle pour sommer les entiers
    while (iter <= n):
        # Ajoute la valeur à sum
        sum += iter
        # Augmente la valeur de la variable d'itération
        iter += 1
    # Retourne la valeur de la somme
    return sum

# Solution du probleme 
def factorielle(n):
    """
    Fonction pour obtenir la valeur de n!. (Expliquez la définition de n! avant)
    Peut se faire à l'aide de boucle ou de récursion.

    Notions à savoir:
        - Opération simple (addition, soustraction, multiplication)
        - Boucle (while, for)
    """
    # Initialise une variable pour stocker la valeur de n!
    resultat = n
    # Initialise une variable d'itération
    iter = n-1
    # Boucle sur tous les entiers non-nuls inférieurs à n
    while(iter > 0):
        # Multiplie résultat par iter
        resultat *= iter
        # Reduit la valeur de iter
        iter -= 1
    # Retourne la valeur de resultat
    return resultat

# Solution du probleme
def inverseLeMot(mot):
    """
    Fonction pour obtenir l'inverse du mot fourni en argument.
    Exemple: Fermion -> noimreF

    La fonction peut se faire en une ligne en utilisant les opérations
    built-in des liste en python, soit mot[::-1]. Cependant, si un jeune
    utilise cette solution, demandez-lui de faire sa propre fonction.

    Notions à savoir:
        -
    """
    # Initialise le mot qui sera retourné
    mot_inv = ""
    # Boucle sur le mot original
    for i in range(0, len(mot)):
        # Ajoute le caractère de mot à mot_inv
        mot_inv += mot[-(1+i)] # Traverse le mot à l'envers
    # Retourne le mot inversé
    return mot_inv

# Solution du probleme
def obtenirMax(liste):
    """
    Fonction pour obtenir le plus grand nombre de la liste en argument.
    Ne pas utiliser la fonction built-in «max()», ca serait assez plate.

    Notions à savoir:
        - Manipulation de liste (index)
        - Boucle (for)
        - Opération logique (<, >, ==, etc.)
    """
    # Initialise la valeur du nombre qui sera retourn.
    nombreMax = liste[0]
    # Boucle sur les autres éléments de la liste
    for i in range(1, len(liste)):
        # Vérifie si nombreMax est plus petit que le nombre de la liste
        if (nombreMax < liste[i]):
            # Met à jour la valeur de nombreMax
            nombreMax = liste[i]
    # Retourne nombreMax
    return nombreMax

# Solution du probleme 
def heureEnSecondes(x, y, z):
    """
    Fonction pour convertir un temps du format (h, m, s)
    au format (s). Exemple: 1:00:42 (1h00m42s) -> 3642s

    Notions à savoir:
        - Convertion heure, min -> secondes
        - Manipulation de variables
        - Opération simple (addition, multiplication)
    """
    # Convertion d'une heure, minute, en seconde
    h = 3600    # (1h = 3600 sec)
    m = 60      # (1m = 60 sec)
    # Initialise une variable pour stocker la convertion
    s = z   # z == nombre de secondes
    # Ajoute les minutes
    s += y * m  # Ajoute le nombre de minutes en secondes
    # Ajoute les heures
    s += x * h  # Ajoute le nombre d'heures en secondes
    # Retroune la valeur finale
    return s

# Solution du probleme 
def secondeEnHeures(sec):
    """
    Fonction pour convertir un nombre de seconde en temps sous le format
    xh:y:z. Ce qui est retourné doit être un string!
    Exemple: 3661s -> 1h:1m:1s 

    Notions à savoir:
        - Convertions heure, minutes, secondes
        - Opérations (addition, soustraction, division entière, multiplication)
        - Manipulation de string (addition, convertion int -> string)
    """
    # Initialise le mot qui sera retourné
    temps = ""
    # Convertion heure, minute en secondes
    h = 3600
    m = 60
    # Détermine le nombre d'heure entière que le input contient
    x = sec // h
    # Soustrait le nombre de secondes correspondant à la valeur initiale
    restant = sec - (x * h)
    # Détermine le nombre de minutes entière que la nouvelle valeur de s contient
    y = restant // m
    # Soustrait le nombre de seconde correspondant
    restant -= (y * m)
    # Converti le résultat en string
    temps += (str(x) + "h:" + str(y) + "m:" + str(restant) + "s")
    return temps

# Solution du probleme
def obtenirAge(dateDeNaissance):
    """
    Function pour obtenir l'age d'une personne selon la date fournie
    en input. Le format de la date devrait etre «yyyy/mm/dd».

    Notions à savoir:
        - Manipulation de string (.split())
        - Manipulation de listes (index)
        - Opération logique
    """
    # Sépare les éléments de la date
    dateNaissanceSplit = dateDeNaissance.split("/")
    # Convertie et associe les valeurs
    aNaissance = int(dateNaissanceSplit[0])
    mNaissance = int(dateNaissanceSplit[1])
    jNaissance = int(dateNaissanceSplit[2])
    # Première approximation de l'age selon la différence des années
    age = YEAR - aNaissance
    # Corrige l'erreur fait sur les mois
    if (MONTH < mNaissance) :
        # Corrige l'Age
        age -= 1
    # Vérifie si le mois de naissance et actuel sont les meme
    elif (MONTH == mNaissance) :
        # Corrige l'erreur fait sur les jours
        if (DAY < jNaissance) :
            # Corrige l'age
            age -= 1
    # Retourne l'age
    return age

# Solution du probleme
def convertirAgeEnSeconde(age):
    """
    Fonction pour convertir l'âge d'une personne en secondes.
    Il est assumé que l'argument «age» est de type int.

    Notions à savoir:
        - Convertions minute;heure;jour;annee
    """
    # Convertion de minute -> heure -> jour
    m = 60      # 1 minute == 60 secondes
    h = 60 * m  # 1 heure == 60 minutes
    j = 24 * h  # 1 jour == 24 heures
    a = 365 * j # 1 ans == 365 jours
    # Converti l'age en seconde
    temps_sec = (age * a)
    # Retourne la valeur
    return temps_sec

# Solution du probleme 
def convertirSecondeEnAge(sec):
    """
    Fonction pour convertir un nombre de secondes en age (années).
    Il est assumé que l'argument «sec» est de type int.

    Notions à savoir:
        - Possible d'utiliser une fonction dans une autre fonction.
    """
    # Convertion
    a = convertirAgeEnSeconde(1)    # Obtient le nombre de seconde d'une année
    # Obtient le nombre d'année compris dans le temps en seconde
    temps = sec / a
    # Retourne la valeur de temps<
    return temps

# solution du probleme
def convertirAnniversaire():
    """
    Fonction qui demandera l'anniversaire de l'utilisateur sour le format (yyyy/mm/dd)
    et qui le convertie sous le format day month year.
    """
    # Tuple des mois possible
    month = ('Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre')
    # Demande à l'utilisateur sa date d'anniversaire
    date = input("Quel est votre date d'anniversaire? (yyyy/mm/dd) ")
    # Sépare la date à chaque '/'
    date_split = date.split("/")
    # Obtient la date sous le nouveau format
    date_new = date_split[2] +" "+ month[int(date_split[1])-1] +" "+ date_split[0]
    # Retourne la date
    return date_new

# Solution du probleme
def obtenirNombrePair(n):
    """
    Fonction pour obtenir les «n» premiers nombre pairs et les places dans une liste.
    """
    # Créer une liste vide
    nombres = []
    # Boucle tant que la liste n'est pas remplie
    i = 0
    while (len(nombres) != n):
        nombres.append(i)
        i += 2
    # Retourne la liste
    return nombres

# Solution du probleme
def obtenirNombreimpair(n):
    """
    Fonction pour obtenir les «n» premiers nombres impairs.
    """
    # Créer une liste vide
    nombres = []
    # Boucle tant que la liste n'est pas remplie
    i = 1
    while (len(nombres) != n):
        nombres.append(i)
        i += 2
    # Retourne la liste
    return nombres

# Solution du probleme 
def estPair(k):
    """
    Fonction pour déterminer si le nombre «k» est pair.
    Sans l'utilisation de la fonction modulo et '&'.
    """
    while (k > 0):
        k -= 2
    return k == 0


testSolution(inverseCaps, "AbcDEFGhIuGa")
testSolution(nombreDeVoyelles, "Allo, what's up?")
testSolution(plusLongMot, "Quel est le plus long mot de cette phrase?")
testSolution(somme, 10)
testSolution(factorielle, 10)
testSolution(inverseLeMot, "Fermion")
testSolution(obtenirMax, [0, 15, 100, 45, 78, 42])
testSolution(heureEnSecondes, 1, 1, 1)
testSolution(secondeEnHeures, 3661)
testSolution(obtenirAge, "1995/08/21")
testSolution(convertirAgeEnSeconde, 23)
testSolution(convertirSecondeEnAge, obtenirFactorielle(10))
#testSolution(convertirAnniversaire)
testSolution(obtenirNombrePair, 10)
testSolution(obtenirNombreimpair, 10)
testSolution(estPair, 15)