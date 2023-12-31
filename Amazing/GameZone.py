import pygame
import pygame.draw

from Const import *


"""
    Classe zone représente la zone du jeu (zone qu'occupera le labyrinthe à l'écran)
    """
class Zone:


    def __init__(self, width: int, height: int):

        self.height = height
        self.width = width

        self.game_surface = pygame.Surface((self.height, self.width))
        self.game_surface.fill(NONE)

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width




