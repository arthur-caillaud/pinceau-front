# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

class Employee: # Définition de notre classe Employee
   
    def __init__(self, nom, prenom): # Notre méthode constructeur
        """Pour l'instant, on ne va définir qu'un seul attribut"""
        self.nom = nom
        self.prenom = prenom
        
bernard=Employee("fort", "bernard")
print(bernard.prenom)
        
