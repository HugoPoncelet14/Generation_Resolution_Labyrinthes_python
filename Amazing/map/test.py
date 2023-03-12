import pygame

class test:

    def __int__(self, posx, posy, height, width, surface, couleur):

        self.posx = posx
        self.posy = posy
        self.height = height
        self.width = width
        self.surface = surface
        self.couleur = couleur

        rect = (posx, posy, height, width)
        pygame.draw.rect(surface,couleur,rect)



