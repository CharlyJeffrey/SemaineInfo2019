# DÉFI PYTHON 

## Solutions

__HelloWorld__
```python
def HelloWorld():
    # Demande le nom de la personne
    nom = input("Quel est votre nom? ")
    # Demande l'âge de la personne
    age = input("Quel est votre âge? ")
    # Demande à la personne une chose qu'elle aime
    aime = input("Nommez une chose que vous aimez: ")
    # Affiche un petit message amicale
    print("Bonjour " +nom+ ", vous avez " +age+ " ans et aimez " +aime)
```

__inverseCaps__
```python
def inverseCaps(mot):
    # Toutes les lettres en minuscules
    lettres = "abcdefghijklmnopqrstuvwxyz"
    # Initialise le mot qui sera retourné
    mot_inv = ""
    # Boucle sur le mot original
    for l in mot:
        # Vérifie si la lettre (l) est minuscule
        if l in lettres:
	    # Ajoute la lettre en majuscule à mot_inv
	    mot_inv += l.upper()
	# Sinon la lettre est une majuscule
	else:
	    # Ajoute la lettre en minuscule à mot_inv
	    mot_inv += l.lower()
    # Affiche le nouveau mot
    print(mot_inv) 
```

__inverseLeMot__
```python
def inverseLeMot(mot):
    # Initialise un mot vide
    mot_inv = ""
    # Boucle sur le mot original
    for i in range(len(mot)):
        # Ajoute le caractère à mot_inv
        mot_inv += mot[-(1+i)]
    # Affiche le mot inversé
    print(mot_inv)
```

__nombreDeVoyelles__
```python
def nombreDeVoyelles(phrase):
    # Toutes les voyelles de l'alphabet
    voyelles = "aeiouy"
    # Compteur du nombre de voyelle
    nombre_voyelles = 0
    # Boucle sur toutes les caractères de la phrase
    for c in phrase:
        # Vérifie si le caractère est une voyelle
        if c.lower() in voyelles:
            # Augmente les compteur
            nombre_voyelle += 1
    # Affiche la valeur du compteur
    print(nombre_voyelle)
```

__somme__
```python
def somme(n):
    # Initialisation d'une variable pour stocker la valeur d ela somme
    sum = 0
    # Boucle sur tous les entiers entre 1 et n
    for i in range(1, n+1):
        # Ajoute la valeur de i à sum
        sum += i
    # Affiche la valeur de sum
    print(sum)
```

__factorielle__
```python
def factorielle(n):
    # Initialise une variable pour stocker la valeur de n!
    resultat = 1
    # Boucle sur les entiers entre 1 et n, inclusivement
    for i in range(1, n+1):
        # Multiplie le resultat par i
        resultat *= i
    # Affichela valeur de resultat
    print(resultat)   
```

__estPair__
```python
def estPair(k):
    # Enlève 2 à k tant que le résultat est plus grand que 0
    while (k > 0):
        k -= 2
    # Affiche True si k vaut 0 après la boucle
    print(k == 0)
```

__obtenirMax__
```python
def obtenirMax(liste):
    # Initialise une variable pour stocker la valeur temporaire du maximum
    max_temp = liste[0]
    # Boucle sur tous les éléments de la liste
    for i in range(1, len(liste)):
        # Vérifie si l'élément de la liste est plus grand que le maximum actuelle
        if (liste[i] > max_temp):
            # Change la valeur du maximum actuelle 
            max_temp = liste[i]
    # Affichela valeur de max_temp
    print(max_temp)
```

__obtenirAge__
```python
"""!!!Seulement si la date actuelle n'est pas manuellement entrée!!!"""
import datetime
now = str(datetime.datetime.now())
ANNEE = int(now[0:4])
MOIS = int(now[5:7])
JOUR = int(now[8:10])
"""!!!Si la date actuelle est manuellement entrée!!!"""
ANNEE = 2018
MOIS = 09
JOUR = 17

def obetnirAge(date):
    # Séprare la date entrée à chaque '/'
    date_split = date.split('/')
    # Convertie les valeurs en int et les associe à des variables        
    annee_naissance = int(date_split[0])
    mois_naissance = int(date_split[1])
    jour_naissance = int(date_split[2])
    # Première approximation de l'âge selon la différence entre les années
    age = ANNEE - annee_naissance
    # Corrige l'erreur fait avec les mois
    if (MOIS < mois_naissance):
        age -= 1
    # Vérifie si le mois de naissance et actuel sont les même
    elif (MOIS == mois_naissance):
        # Corrige l'erreur fait sur les jours
            if (JOUR < jour_naissance):
                age -= 1
    # Affichel'âge
    print(age)
```

__convertirAge__
```python
def convertirDate(date):
    # Tuple de tous les mois
    liste_mois = ('Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre')
    # Sépare la date à chaque '/'
    date_split = date.split('/')
    # Associe à des variables le jours, le mois et l'année
    jour = date_split[2]
    mois = int(date_split[1])
    annee = date_split[0]
    # Affiche la date sous le nouveau format
    print(jour +" "+ date_liste[mois] +" "+ annee)
```

__plusLongMot__
```python
def plusLongMot(phrase):
    # Caractères à ne pas ignorer
    carac = "abcdefghjiklmnopqrstuvwxyz"
    # Initialise un mot vide
    mot_long = ""
    # Sépare la phrase à chaque espace
    phrase_split = phrase.split()
    # Boucle sur tous les éléments de la phrase séparée
    for m in phrase_split:
        # Initialise un mot vide
        mot = ""
        # Boucle sur le mot actuelle pour enlever toute ponctuation
        for c in m:
            # Vérifie si le caractère fait partie de carac
            if c.lower() in carac:
                # Ajoute le caractère à mot
                mot += c
        # Vérifie si la longuer du mot (sans la ponctuation) est plus grande
        if (len(mot) > len(mot_long)):
            # Un nouveau mot plus long a été trouvé
            mot_long = mot
    # Affichele mot le plus long
    print(mot_long)

```


