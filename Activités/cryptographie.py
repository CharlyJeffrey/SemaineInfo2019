""" Activité de cryptographie
"""

import numpy as np
import random as rd
from Ciphers import Cipher

def caesar_decoder(cipher: str, key: int, alph: str, MAP: dict):
    """caesar_decoder Fonction pour décoder le chiffrement de Caesar
    
    Args:
        cipher (str): Chiffrement à décoder
        key (int): Clé à utiliser
        alph (str): Alphabet utilisé
        MAP (dict): Mapping des lettres
    
    Returns:
        msg (str): Message déchiffré
    """
    MOD = len(alph)
    # Initialise le message
    msg = ""
    # Boucle sur tous les charactères du chiffrement
    for l in cipher:
        # Vérifie si le charactère fait partie de l'alphabet
        if l.lower() in alph:
            # Détermine la position de la lettre originale
            index = (MAP[l.lower()] - key) % MOD
            # Ajoute la lettre
            msg += alph[index]
        else:
            # Ajoute le charactère
            msg += l
    # Retourne le message déchiffré
    return msg


CIPHER = Cipher()
alph = CIPHER.get_alph()
MAP = CIPHER.get_map()

cipher = CIPHER.caesar("Allo")

# Teste les clés de 0 à 25
for i in range(len(alph)):
    # Obtient le message selon la 'ie' clé
    msg = caesar_decoder(cipher, i, alph, MAP)
    if (CIPHER.caesar_bonne_cle(msg, "Allo")):
        break

print(msg, i)