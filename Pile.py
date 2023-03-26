#!/usr/bin/env python3
# -*- coding: utf-8 -*-



class Pile_lst:
    """Implémentation d'une pile par une liste."""
    def __init__(self):
        """Crée une pile vide."""
        self.__pile = []

    def est_vide(self):
        """Indique si la pile est vide."""
        return self.__pile == []

    def empiler(self, valeur):
        """Empile la valeur."""
        self.__pile.append(valeur)

    def depiler(self):
        """Dépile le sommet de la pile et le renvoie."""
        return self.__pile.pop()

    def taille(self):
        """Renvoie la taille de la pile."""
        return len(self.__pile)

    def sommet(self):
        """Renvoie le sommet de la pile (sans le dépiler)."""
        return self.__pile[-1]

    def __str__(self):
        s = "|"
        for val in self.__pile:
            s = str(val) + "->" + s
        return s



