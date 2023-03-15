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
laby.gen_exploration()




bords = pygame.Surface((408, 408))
bords.fill(Const.WHITE)
surface.blit(bords, (36, 36))

jeu = laby.surface.game_surface
jeu.fill(Const.BLACK)
maze = laby.afficher(jeu)
surface.blit(maze,(40, 40))

police = pygame.font.Font("font/8-bit-pusab.ttf", 16)
text_surface = police.render("AMAZING", True, Const.WHITE)
surface.blit(text_surface, (175, 5))

image = pygame.image.load("images/the-rock-sus.png")
image = pygame.transform.scale(image, (40,40))
surface.blit(image, (40, 40))

x = 40
y = 40
xc = 0
yc = 0
pos = (x, y)
pos = (x, y)
posc = (xc, yc)
while pos != (400, 400):

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT:
                if (xc+1, yc) in laby.laby.get_reachable_cells(posc):
                    x += 40
                    xc += 1
                    pos = (x, y)
                    posc = (xc, yc)
                    print(pos, posc)
                    surface.blit(maze, (40, 40))
                    surface.blit(image, pos)

            if event.key == pygame.K_LEFT:
                if (xc-1, yc) in laby.laby.get_reachable_cells(posc):
                    x -= 40
                    xc -= 1
                    pos = (x, y)
                    posc = (xc, yc)
                    print(pos, posc)
                    surface.blit(maze, (40, 40))
                    surface.blit(image, pos)

            if event.key == pygame.K_DOWN:
                if (xc, yc+1) in laby.laby.get_reachable_cells(posc):
                    y += 40
                    yc += 1
                    pos = (x, y)
                    posc = (xc, yc)
                    print(pos, posc)
                    surface.blit(maze, (40, 40))
                    surface.blit(image, pos)


            if event.key == pygame.K_UP:
                if (xc, yc-1) in laby.laby.get_reachable_cells(posc):
                    y -= 40
                    yc -= 1
                    pos = (x, y)
                    posc = (xc, yc)
                    print(pos, posc)
                    surface.blit(maze, (40, 40))
                    surface.blit(image, pos)




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













