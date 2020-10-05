#! /usr/bin/env python
# @carolio7

# importation des bibliothèques
from random import randint, seed

from enum import Enum

import matplotlib.pyplot as plt

import numpy as np


# les stratégies possibles
class Strategie(Enum):
    CHANGER = 1
    GARDER = 2

seed()

def monty_hall(strategie, nb_tour):
    """Fonction simule le jeux Monty Hall 
    avec les nombre de parties joué en utilisant Numpy
    sans boucle 'for' 

    Args:
    	strategie(Strategie): la strategie du joeur au deuxième choix,
    	nb_tours : le nombre de partie jouées

    Returns:
    	np.ndarray: matrice à une dimmension avec 1 le nombre de parties gagnées et 0 les parties perdues
    """

    #Création d'array qui contiendra les parties à jouer 
    resultats = np.arange(0, nb_tour)
    

    i = 0
    while i < nb_tour:
        # les trois portes à choisir
        portes = np.arange(3)
    
        # le premier choix du joueur
        premier_choix = np.random.choice(portes)
    
        # la porte avec la voiture
        bonne_porte = np.random.choice(portes)
    
        # Exclusion de la porte choisie parmi ceux que le présentateur va éliminer
        portes = np.delete(portes, premier_choix)
    
        if premier_choix == bonne_porte:
            # Le présentateur élimine au hasard un des deux portes sans voitures
            portes = np.delete(portes, np.random.choice(np.arange(2)))
        else:
            # On garde seulement la porte avec la voiture si le joueur n'a pas choisie la bonne
            portes = np.array([bonne_porte])
    
        deuxieme_choix = np.array([])

        if strategie == Strategie.CHANGER:
            deuxieme_choix = portes[0]
        elif strategie == Strategie.GARDER:
            deuxieme_choix = premier_choix
        else:
            raise ValueError("Stratégie non reconnues!")
        
        if deuxieme_choix == bonne_porte:
            resultats[i] = 1
        else:
            resultats[i] = 0
        # On aurait pu écrire sous-forme comprehesion list comme ceci: 
        #resultat[i] = 1 if deuxième_choix == bonne_porte else 0
        # Ce serait moins parlant à lire le code plus tard
        

        # On joue le prochain parties
        i += 1
        
    return resultats
