# coding: utf-8


""" 
Petit document resumant quelques notions de Python.

Workflow habituelle d'un script python:

    - Desciption du script / Copyright

    - Importation des librairies

    - Définition des variables globales (GLOBAL_VARIABLE_NOMENCLATURE)

    - Définition des fonctions / classes

    - Script (== main() en C/C++)

"""
from sys import getsizeof
# Librairie très importante pour opération sur des arrays (de manière efficace)
import numpy as np 
# Librairie pour obtenir différentes distributions de nombres aléatoires
import random as rd
# Librairie pour obtenir le temps
import time


""" Section no 1:
* Variables & types
* Fonction 'print()'
* Fonction 'input()'
* Méthode '.format()'
"""

# Python n'est pas un langage typé tels que Java, C/C++, etc.
# Une variable doit donc être instanciée avec un symbole et une valeur, mais sans préciser son type.
# La valeur d'une variable peut être modifée à tout moment et son type s'adaptera en conséquence.

# Les types possibles sont : bool, int, float, string.
# Python s'occupe de gérer la mémoire alouée pour les int/float; un 'int' trop long devient une 'long' automatiquement.
# Il n'y a pas de 'char' en Python; tout est considéré comme un 'string'. On peut utilisé ' ' ou " ".
# ***Nomenclature: lower_case ou mixedCase***

# Les opérations que l'on peut faire avec les 'int/float' sont assez simple: +, -, *, /, //, %, **, ^, etc.
# Python permet facilement de concatener des 'string' en utilisant l'addiction: str_a + str_b = str_c
# On peut également multiplier un string par un 'int' qui résulte à le string concatené avec lui-même 'x' fois.
# Similairement au langage C (puisque Python est interprété en C), un string n'est qu'en fait un array de 'char'.


a = 2   # Une variable doit être instancité avec une valeur!
b = ""  # Convention pour initialiser un string vide
b = input("Entrez votre nom: ") # Obtient une valeur auprès de l'utilisateur
c = "Allo " + b
# Différente méthode pour afficher dans la console
print(a, b, c)
print("{} {} {}".format(a, b, c))
print(f"{a} {b} {c}")
print("\n")   # <-- Caractère de saut de ligne





""" Section no 2:
* if/elif/else statement
* Fonction 'range()'
* Boucle 'for'
* Boucle 'while'
"""


# Python utilise les statements 'if-else if-else' de manière similaire à d'autre langage.
# Si la condition du 'if' est vrai, alors uniquement son statement sera exécuté;
# Sinon, l'interprète continue dans la chaîne de 'elif' jusqu'à ce qu'une condition est vrai;
# Dans le cas où aucune expression est vraie, alors le statement du 'else' sera exécuté.
# Nomenclature:
#               if (condition_one):
#                   <statement_one>
#               elif (condition_two):
#                   <statement_two>
#               ...
#               else:
#                   <statement>
#               <statement> (Reste du code)

x = rd.randint(0, 10)
y = rd.randint(0, 10)

if (x >= y and y < 5):
    if (x > 7):
        print("Cas no 1.")
    elif (x == y):
        print("Cas no 2")
    else:
        print("Cas no 3")
else:
    print("Cas no 4")
    


# Pour généré une suite de nombres rapidement, on peut utiliser la fonction 'range([start], end, [step])'.
# Cette fonction prend trois arguments: 
#   start (optionnel)   : Premier nombre de la suite;   0 par défaut
#   end                 : Dernier nombre (exclu) de la suite générée
#   step (optionnel)    : Pas entre les nombres générés;0 par défaut
#
# La fonction range n'est en fait qu'une fonction génératrice. 
# Les fonctions génératrices permettent de générer une suite de nombre respectant une certaine condition,
# et ce, de manière très efficace.

x_min, x_max = 5, 100
liste_one = range(x_max)            # Ensemble des nombres [0, 100[
liste_two = range(x_min, x_max)     # Ensemble des nombres [5, 100[
liste_thr = range(x_min, x_max, 3)  # Ensemble des nombres [5, 100[ par pas de 3


# Les boucles 'for' en Python sont assez uniques: elles peuvent uniquement itérer sur une liste d'élément.
# Lorsqu'on veut faire 'x' itérations, alors la fonction -génratrice- range(X) est utilisée. 
# Nomenclature:
#               for (var in list):
#                  <statement> (fait partie de la boucle)
#               <statement> (ne fait pas partie de la boucle)

for x in liste_one:
    pass
    #print(x)
print()

for x in liste_two:
    for y in liste_thr:
        if x == y:
            pass
            #print(x)

# Les boucle 'while' en python sont similaires aux autres langages: pour que la boucle puisse itérer,
# la condition doit être 'True'. Un compteur peut être utilisé, mais doit être instancié avant l'entrée.
# Nomenclature:
#               while (condition):
#                   <statement> (fait partie de la boucle)
#               <statement> (ne fait pas partie de la boucle)

i = 0
n = 0
while(i < 256):
    n = n << 1
    #print(n)
    i += 1  # <-- Équivalent à 'i++' de C. 

""" Section no 3:
* Listes & tuples
* Array (numpy)
"""

# Les listes en Python sont similaires aux tableaux que l'on retrouve dans d'autres langages;
# L'objet 'list' vient avec plusieurs méthodes dont '.append()' et 'pop()'. Les listes sont
# des objets modifiables en Python. Lorqu'une liste est instanciée, sa taille ne doit pas être précisée.
#
# Les tuples ne sont en fait que des listes, mais ne peuvent pas être modifiés une fois instanciés!
# Donc plus rapide à utiliser et optimise la mémoire.
#
# Pour déterminer la taille d'une liste en Python, la donction 'len()' doit être utilisée;
# celle-ci prend une liste en argument et retourne sa taille (nombre d'élément).
#
# Les 'arrays' de la librairie 'numpy' sont très puissant et peuvent être vu comme une version
# amiliorée des listes de Python; permet de vectoriser (parallèliser) et ainsi d'éviter de faire de boucles.

start = time.time()
liste_one = []  # Initialise une liste vide
# Ajoute à la liste tous les nombres entre 0 et 100 (exclu)
for i in range(1000000):
    liste_one.append(i)
end = time.time()
delta_one = end - start

# Même chose que plus haut, mais de manière ridiculement plus efficace
start = time.time()
liste_two = [i for i in range(1000000)]
end = time.time()
delta_two = end - start

print(f"First list: {delta_one}; Seconde list: {delta_two}; Ration : {delta_one/delta_two}")

""" Section no 4:
* Fonction
"""

# Python permet la programmation fonctionnelle. Puisque Python est un langage interprété, lorsqu'une fonction
# est appelée, sa définition doit déjà avoir été interprètée avant l'appel. Tel que mentionné, Python n'est pas
# un langage typé et donc lorsqu'une fonction est définie, uniquement ses arguements et son corps doivent être
# précisés. Une fonction en Python peut retourner plusieurs choses; dans un tel cas, ce qui est retourné
# n'est tant fait qu'un tuple qui contient les élément retournés.
#
# Nomenclature:
# (Définition)
#               def nomDeLaFonction(argument_un, argument_deux, ...):
#                   <statement>
#                   return <var> ou <tuple>
# (Appel)
#               <var> = nomDeLaFonction(argument_un, argument_deux, ...)
#                 ou
#               <var1>, <var2>, ... = nomDeLaFonction(argument_un, argument_deux, ...)


def fibo(n : int):
    """fibo Fonction inéfficace pour générer la suite de Fibonacci.
    
    Args:
        n (int): Nombre d'élément à générer
    """
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

# Dictionnaire utilisé comme cache
CACHE = {}
def fibo_memoization(n : int):
    """fibo_memoization Fonction éfficace pour générer la suite de Fibonacci
    
    Args:
        n (int): Nombre d'élément à générer
    """
    # Vérifie si le n ieme nombre a été calculé
    if n in CACHE:
        # Retourne le nombre associé
        return CACHE[n]
    # Sinon calcule le n ieme nombre
    if n == 1 or n == 2:
        _v = 1
    else:
        _v = fibo_memoization(n-1) + fibo_memoization(n-2)
    
    # Ajoute la valeur à la cache
    CACHE[n] = _v
    # Retourne la valeur 
    return _v

# Test de la premiere fonction (seule)
start = time.time()
fibo(35)
end = time.time()
delta_one = end - start 

# Test de la deuxième fonction (avec memoization)
start = time.time()
fibo_memoization(35)
end = time.time()

print(f"Time 1: {delta_one}; Time 2: {delta_two}; Ratio: {delta_one/delta_two}")