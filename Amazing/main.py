import sys
import pygame.draw

from Const import *
from map.GameZone import Zone
from map.maze import Maze


pygame.init()

# Création de la fenêtre
pygame.display.set_caption('The Rocklike (the rock, roguelike vous avez compris ?)')
surface = pygame.display.set_mode((480, 720))


#Création du labyrinthe
jeu = Zone(400,400)
laby = Maze(jeu, 10, 400, True)
laby.gen_exploration()
bords = pygame.Surface((408, 408))
bords.fill(WHITE)
surface.blit(bords, (36, 36))
jeu = laby.surface.game_surface
jeu.fill(BLACK)
maze = laby.afficher(jeu)
surface.blit(maze,(40, 40))

#Création de l'interface
police = pygame.font.Font("font/8-bit-pusab.ttf", 16)
text_surface = police.render("THE ROCKLIKE", True,WHITE)
surface.blit(text_surface, (125, 5))

#Création du joueur
image = pygame.image.load("images/the-rock-sus.png")
image = pygame.transform.scale(image, (40,40))
surface.blit(image, (40, 40))

#Déplacements du joueur
x = 40
y = 40
xc = 0
yc = 0
pos = (x, y)
posc = (xc, yc)
coups = 0
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
                    coups += 1

            if event.key == pygame.K_LEFT:
                if (xc-1, yc) in laby.laby.get_reachable_cells(posc):
                    x -= 40
                    xc -= 1
                    pos = (x, y)
                    posc = (xc, yc)
                    print(pos, posc)
                    surface.blit(maze, (40, 40))
                    surface.blit(image, pos)
                    coups += 1

            if event.key == pygame.K_DOWN:
                if (xc, yc+1) in laby.laby.get_reachable_cells(posc):
                    y += 40
                    yc += 1
                    pos = (x, y)
                    posc = (xc, yc)
                    print(pos, posc)
                    surface.blit(maze, (40, 40))
                    surface.blit(image, pos)
                    coups += 1

            if event.key == pygame.K_UP:
                if (xc, yc-1) in laby.laby.get_reachable_cells(posc):
                    y -= 40
                    yc -= 1
                    pos = (x, y)
                    posc = (xc, yc)
                    print(pos, posc)
                    surface.blit(maze, (40, 40))
                    surface.blit(image, pos)
                    coups += 1

            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


#Ecran de fin
surface.blit(maze, (40, 40))
win = pygame.image.load("images/the-sus.png")
surface.blit(win, (50, 540))

police = pygame.font.Font("font/8-bit-pusab.ttf", 64)
text_surface = police.render("GG !", True, WHITE)
surface.blit(text_surface, (225, 580))

police = pygame.font.Font("font/8-bit-pusab.ttf", 10)
text_surface = police.render("APPUYEZ SUR ENTRER POUR CONTINUER _", True, WHITE)
surface.blit(text_surface, (50, 520))

police = pygame.font.Font("font/8-bit-pusab.ttf", 10)
text_surface = police.render("vous avez termine le labyrinthe en "+str(coups)+" coups", True, WHITE)
surface.blit(text_surface, (50, 460))

police = pygame.font.Font("font/8-bit-pusab.ttf", 10)
text_surface = police.render("le minimum de coups possible etait "
                             +str(laby.len_solve_dfs((0, 0), (laby.taille-1, laby.taille-1))-1)+" coups"
                             , True, WHITE)
surface.blit(text_surface, (50, 480))

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
            if event.key == pygame.K_RETURN:

                #Création de l'écran de fin
                surface.fill(BLACK)

                police = pygame.font.Font("font/8-bit-pusab.ttf", 30)
                text_surface = police.render("Merci ! ", True, WHITE)
                surface.blit(text_surface, (150, 210))

                police = pygame.font.Font("font/8-bit-pusab.ttf", 12)
                text_surface = police.render("Merci d'avoir joue au jeu", True, WHITE)
                surface.blit(text_surface, (100, 260))

                police = pygame.font.Font("font/8-bit-pusab.ttf", 10)
                text_surface = police.render("Si vous etes ici c'est que vous avez reussi a", True, WHITE)
                surface.blit(text_surface, (40, 280))
                text_surface = police.render("sauver The Rock de ce labyrinthe miteux", True, WHITE)
                surface.blit(text_surface, (50,300))
                text_surface = police.render("Mais ne prenez pas trop la grosse tete", True, WHITE)
                surface.blit(text_surface, (55, 320))
                text_surface = police.render("Car the rock en a une plus gros que vous", True, WHITE)
                surface.blit(text_surface, (55, 340))
                text_surface = police.render("enfin bref, ce jeu n'est pas fini d'etre developpe", True, WHITE)
                surface.blit(text_surface, (25, 370))
                text_surface = police.render("Alors si vous voulez re faire une partie,", True, WHITE)
                surface.blit(text_surface, (50, 390))
                text_surface = police.render("faites echap et re executez le script, ciao :)", True, WHITE)
                surface.blit(text_surface, (30, 410))


    # Mise a jour de l'affichage
    pygame.display.flip()













