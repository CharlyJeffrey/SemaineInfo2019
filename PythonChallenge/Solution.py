"""
Solution des défis python
"""

def testSolution(func, *args, **kargs):
    """
    Fonction pour tester une certaine fonction donnée en argument.
    Affiche le résultat de la fonction
    """
    print(func(*args, **kargs))

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
def obtenirFactorielle(n):
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
def secondeEnHeures(s):
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
    x = s // h
    # Soustrait le nombre de secondes correspondant à la valeur initiale
    s -= x * h
    # Détermine le nombre de minutes entière que la nouvelle valeur de s contient
    y = s // m
    # Soustrait le nombre de seconde correspondant
    s -= y * m
    # Converti le résultat en string
    temps += (str(x) + "h:" + str(y) + "m:" + str(s) + "s")
    return temps


testSolution(inverseCaps, "AbcDEFGhIuGa")
testSolution(nombreDeVoyelles, "Allo, what's up?")
testSolution(plusLongMot, "Quel est le plus long mot de cette phrase?")
testSolution(somme, 10)
testSolution(obtenirFactorielle, 5)
testSolution(inverseLeMot, "Fermion")
testSolution(obtenirMax, [0, 15, 100, 45, 78, 42])
testSolution(heureEnSecondes, 1, 1, 1)
testSolution(secondeEnHeures, 3661)