from random import randint
class Cipher:

    __slots__ = ('_ALPH', '_MOD', '_MAP', '__CAESAR_KEY', '__CAESAR_MSG')
    def __init__(self):
        # Alphabet utilisé
        self._ALPH = "abcdefghijklmnopqrstuvwxyz"
        self._MOD = len(self._ALPH)
        # Mapping des lettres -> position dans l'alphabet
        self._MAP = {}
        for i in range(len(self._ALPH)): self._MAP[self._ALPH[i]] = i
        # Clé pour le chiffrement de Caesar
        self.__CAESAR_KEY = randint(0, 26)
        # Message utilisé pour le chiffrement de Caesar
        self.__CAESAR_MSG = "Il etait une fois, dans un camp lointain, deux moniteurs tres talentueux. Fermion et Fermionne. Ils formaient un duo de feu et les jeunes les adoraient. Fin."
    
    def get_alph(self): return self._ALPH
    def get_map(self): return self._MAP

    def caesar_bonne_cle(self, msg: str, arg = None):
        """Méthode pour déterminer si la clé trouvé est la bonne.
        
        Args:
            msg (int): Message déchiffré
        
        Returns:
            [bool]: Vrai si la clé est la bonne. Sinon faux.
        """
        if arg is not None:
            MSG = arg
        else:
            MSG = self.__CAESAR_MSG
        for i in range(len(msg)):
            if msg[i].lower() != MSG[i].lower():
                return False
        return True

    def caesar(self, arg = None):
        """Méthode pour chiffrer un message à l'aide du chiffrement de Caesar
        
        Args:
            msg (str): Message à enchiffrer
        
        Returns:
            cipher (str): Message enchiffré
        """
        if arg is not None:
            msg = arg
        else:
            msg = self.__CAESAR_MSG

        # Initialise le message enchiffré
        cipher = ""
        # Boucle sur tous les charactères du message
        for c in msg:
            # Vérifie si le charactère fait partie de l'alphabet
            if c.lower() in self._ALPH:
                # Détermine l'indice de la nouvelle lettre
                index = (self._MAP[c.lower()] + self.__CAESAR_KEY) % self._MOD
                # Ajoute la lettre au cipher
                cipher += self._ALPH[index]
            else:
                cipher += c
        # Retourne le message chiffré
        return cipher


    