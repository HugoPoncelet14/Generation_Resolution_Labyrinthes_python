import pygame
import Amazing.Const
"""
    Classe zone représente la zone du jeu (zone qu'occupera le labyrinthe à l'écran)
    """
class Zone:


    def __init__(self, posx, posy, width: int, height: int):

        self.posx = posx
        self.posy = posy
        self.height = height
        self.width = width

        game_surface = pygame.Surface(self.height, self.width)
        game_surface.fill(Amazing.Const.NONE)
        Amazing.main.surface.blit(self.posx, self.posy)





