from random import *
from cells import Cells
from GameZone import Zone
import Amazing.Const
import pygame


jeu = Zone(400, 400).game_surface

class Maze:

    def __init__(self, surface, taille, side):

        self.surface = Zone(side, side)
        self.cells = Cells(surface, taille)

    def add_wall(self, c1, c2):
        # Facultatif : on teste si les sommets sont bien dans le labyrinthe
        assert 0 <= c1[0] < self.surface.get_height() and \
               0 <= c1[1] < self.surface.get_width() and \
               0 <= c2[0] < self.surface.get_height() and \
               0 <= c2[1] < self.surface.get_width, \
            f"Erreur lors de l'ajout d'un mur entre {c1} et {c2} : les coordonnées de sont pas compatibles avec les dimensions du labyrinthe"
        # Ajout du mur

        if c2 in self.cells[c1]:  # Si c2 est dans les voisines de c1
            self.neighbors[c1].remove(c2)  # on le retire
        if c1 in self.neighbors[c2]:  # Si c3 est dans les voisines de c2
            self.neighbors[c2].remove(c1)  # on le retire