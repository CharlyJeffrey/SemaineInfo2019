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