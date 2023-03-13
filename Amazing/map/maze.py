from random import *
from cells import Cells
from GameZone import Zone
import pygame

jeu = Zone(400, 400).game_surface

cells = Cells()
cells.surface = jeu
cells.nb_cells = 10
cells.create()

class Maze:

    def __init__(self, surface, taille, side):

        self.surface = Zone(side, side)
        self.cells = Cells(surface, taille)