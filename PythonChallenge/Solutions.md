# D�FI PYTHON 

## Solutions

__HelloWorld__
```python
def HelloWorld():
    # Demande le nom de la personne
    nom = input("Quel est votre nom? ")
    # Demande l'�ge de la personne
    age = input("Quel est votre �ge? ")
    # Demande � la personne une chose qu'elle aime
    aime = input("Nommez une chose que vous aimez: ")
    # Affiche un petit message amicale
    print("Bonjour " +nom+ ", vous avez " +age+ " ans et aimez " +aime)
```

__inverseCaps__
```python
def inverseCaps(mot):
    # Toutes les lettres en minuscules
    lettres = "abcdefghijklmnopqrstuvwxyz"
    # Initialise le mot qui sera retourn�
    mot_inv = ""
    # Boucle sur le mot original
    for l in mot:
        # V�rifie si la lettre (l) est minuscule
        if l in lettres:
	    # Ajoute la lettre en majuscule � mot_inv
	    mot_inv += l.upper()
	# Sinon la lettre est une majuscule
	else:
	    # Ajoute la lettre en minuscule � mot_inv
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
        # Ajoute le caract�re � mot_inv
        mot_inv += mot[-(1+i)]
    # Affiche le mot invers�
    print(mot_inv)
```

__nombreDeVoyelles__
```python
def nombreDeVoyelles(phrase):
    # Toutes les voyelles de l'alphabet
    voyelles = "aeiouy"
    # Compteur du nombre de voyelle
    nombre_voyelles = 0
    # Boucle sur toutes les caract�res de la phrase
    for c in phrase:
        # V�rifie si le caract�re est une voyelle
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
        # Ajoute la valeur de i � sum
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
    # Enl�ve 2 � k tant que le r�sultat est plus grand que 0
    while (k > 0):
        k -= 2
    # Affiche True si k vaut 0 apr�s la boucle
    print(k == 0)
```

__obtenirMax__
```python
def obtenirMax(liste):
    # Initialise une variable pour stocker la valeur temporaire du maximum
    max_temp = liste[0]
    # Boucle sur tous les �l�ments de la liste
    for i in range(1, len(liste)):
        # V�rifie si l'�l�ment de la liste est plus grand que le maximum actuelle
        if (liste[i] > max_temp):
            # Change la valeur du maximum actuelle 
            max_temp = liste[i]
    # Affichela valeur de max_temp
    print(max_temp)
```

__obtenirAge__
```python
"""!!!Seulement si la date actuelle n'est pas manuellement entr�e!!!"""
import datetime
now = str(datetime.datetime.now())
ANNEE = int(now[0:4])
MOIS = int(now[5:7])
JOUR = int(now[8:10])
"""!!!Si la date actuelle est manuellement entr�e!!!"""
ANNEE = 2018
MOIS = 09
JOUR = 17

def obetnirAge(date):
    # S�prare la date entr�e � chaque '/'
    date_split = date.split('/')
    # Convertie les valeurs en int et les associe � des variables        
    annee_naissance = int(date_split[0])
    mois_naissance = int(date_split[1])
    jour_naissance = int(date_split[2])
    # Premi�re approximation de l'�ge selon la diff�rence entre les ann�es
    age = ANNEE - annee_naissance
    # Corrige l'erreur fait avec les mois
    if (MOIS < mois_naissance):
        age -= 1
    # V�rifie si le mois de naissance et actuel sont les m�me
    elif (MOIS == mois_naissance):
        # Corrige l'erreur fait sur les jours
            if (JOUR < jour_naissance):
                age -= 1
    # Affichel'�ge
    print(age)
```

__convertirAge__
```python
def convertirDate(date):
    # Tuple de tous les mois
    liste_mois = ('Janvier', 'F�vrier', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Ao�t', 'Septembre', 'Octobre', 'Novembre', 'D�cembre')
    # S�pare la date � chaque '/'
    date_split = date.split('/')
    # Associe � des variables le jours, le mois et l'ann�e
    jour = date_split[2]
    mois = int(date_split[1])
    annee = date_split[0]
    # Affiche la date sous le nouveau format
    print(jour +" "+ date_liste[mois] +" "+ annee)
```

__plusLongMot__
```python
def plusLongMot(phrase):
    # Caract�res � ne pas ignorer
    carac = "abcdefghjiklmnopqrstuvwxyz"
    # Initialise un mot vide
    mot_long = ""
    # S�pare la phrase � chaque espace
    phrase_split = phrase.split()
    # Boucle sur tous les �l�ments de la phrase s�par�e
    for m in phrase_split:
        # Initialise un mot vide
        mot = ""
        # Boucle sur le mot actuelle pour enlever toute ponctuation
        for c in m:
            # V�rifie si le caract�re fait partie de carac
            if c.lower() in carac:
                # Ajoute le caract�re � mot
                mot += c
        # V�rifie si la longuer du mot (sans la ponctuation) est plus grande
        if (len(mot) > len(mot_long)):
            # Un nouveau mot plus long a �t� trouv�
            mot_long = mot
    # Affichele mot le plus long
    print(mot_long)

```


