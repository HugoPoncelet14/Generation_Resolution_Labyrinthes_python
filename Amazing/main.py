import sys
import pygame.draw
import Const
from map.GameZone import Zone
from map.cells import Cells


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



"""pair = 2
for i in range(40, 401, 40):  # 45 = pos x première case, on en met 10 et les cases sont séparés de 40
    for j in range(40, 401, 40):  # 45 = pos y première case
        pygame.display.flip()
        if pair % 2 == 0:
            pygame.draw.rect(surface, Const.WHITE, (i, j, 40, 40))

            print(f"pair{(i, j)}")
        else:
            pygame.draw.rect(surface, Const.BLACK, (i, j, 40, 40))
            print(f"impair {(i, j)}")
        pair += 1
    pair -= 1"""

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













