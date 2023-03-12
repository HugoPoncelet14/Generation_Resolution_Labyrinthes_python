import sys
import pygame.draw
import Const
from map.GameZone import Zone

pygame.init()

#Création de la fenêtre
pygame.display.set_caption('Amazing - Le jeu génial')
surface = pygame.display.set_mode((480, 720))
surface_jeu = Zone(40, 40, 400, 400)



rect = pygame.Rect(0, 0, 40, 720 )
rect2 = pygame.Rect(40, 40, 400, 400)
pygame.draw.rect(surface, Const.ROUGE, rect)

#Essai de création de cases
pair = 2
for i in range(45, 406, 40): #45 = pos x première case, on en met 10 et les cases sont séparés de 40
    for j in range(45, 406, 40):#45 = pos y première case
        pygame.display.flip()
        if pair % 2 == 0:
            pygame.draw.rect(surface, Const.WHITE, (i, j, 40, 40))

            print(f"pair{(i,j)}")
        else:
            pygame.draw.rect(surface, Const.BLACK, (i, j, 40, 40))
            print(f"impair {(i,j)}")
        pair += 1
    pair -= 1




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
    # Mise a jour de l'affichage
    pygame.display.flip()
