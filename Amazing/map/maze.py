from random import *
from cells import Cells
from GameZone import Zone
import Amazing.Const
import pygame


jeu = Zone(400, 400).game_surface

class Maze:

    def __init__(self, surface, taille, side, fill):

        self.surface = Zone(side, side)
        self.cellules = Cells(surface, taille)
        self.fill = fill



