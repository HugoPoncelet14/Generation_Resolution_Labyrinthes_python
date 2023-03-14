import sys
import pygame.draw

import Const
from map.GameZone import Zone
from map.cells import Cells
from map.maze import Maze


pygame.init()

# Création de la fenêtre
pygame.display.set_caption('Amazing - Le jeu génial')
surface = pygame.display.set_mode((480, 720))
jeu = Zone(400, 400).game_surface #A remplacer par maze.zone
surface.blit(jeu , (40, 40))

#Création de repères temporaires
rect = pygame.Rect(0, 0, 40, 720)
pygame.draw.rect(surface, Const.ROUGE, rect)

#Test
jeu = Zone(400,400)
cells = Cells(jeu, 5)
cells.empty()
print(cells.cells)
cells.fill()
print(cells.cells)
cells.remove_wall((0, 0), (0, 1))
print(cells.cells)
print(cells.get_reachable_cells((0,0)))
cells.add_wall((0, 0), (0, 1))
print(cells.cells)
laby = Maze(jeu, 10, 400, True)
print(laby.gen_exploration())

# Boucle de jeu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    # Mise a jour de l'affichage
    pygame.display.flip()













