import pygame
import Amazing.Const


"""
    Classe zone représente la zone du jeu (zone qu'occupera le labyrinthe à l'écran)
    """
class Zone:


    def __init__(self, width: int, height: int):
        import Amazing.main

        self.height = height
        self.width = width

        self.game_surface = pygame.Surface((self.height, self.width))
        self.game_surface.fill(Amazing.Const.NONE)





