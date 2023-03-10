import sys

import pygame

pygame.init()

#Création de la fenêtre
pygame.display.set_caption('Amazing - Le jeu génial')
surface = pygame.display.set_mode((480,720))

#Mise a jour de l'affichage
pygame.display.flip()

#Boucle de jeu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
