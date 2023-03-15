from random import *
import pygame

from Amazing.map.cells import Cells
from Amazing.map.GameZone import Zone
from Amazing.Const import *


class Maze:

    def __init__(self, surface, taille, side, fill):

        self.surface = Zone(side, side)
        self.laby = Cells(surface, taille)
        self.fill = fill
        self.taille = taille

        if self.fill:
            self.laby.fill()

    def gen_exploration(self):
        # Initialisation
        visited = list()
        depart = (randint(0, self.taille - 1), randint(0, self.taille - 1))
        pile = [depart]
        visited.append(depart)
        # Tant que la pile n'est pas vide
        while pile:
            continuer = True
            # La position devient la dernière cellule de la pile et la supprime de la pile
            position = pile.pop()
            voisins = list(self.laby.get_contiguous_cells(position))
            shuffle(voisins)
            i = 0
            while i < len(voisins) and continuer == True:
                # Vérifie si cette cellule a des voisins non visités
                if voisins[i] not in visited:
                    # On ajout le position à la pile
                    pile.append(position)
                    # On casse le mur
                    self.laby.remove_wall(position, voisins[i])
                    # On ajoute la cellule à la pile et aux cellules visités
                    visited.append(voisins[i])
                    pile.append(voisins[i])
                    continuer = False
                i += 1
        return self.laby


    def afficher(self, surface):

        for i in self.laby.cells.keys():
            s = pygame.Surface((self.surface.get_height()//self.taille, self.surface.get_width()//self.taille))
            s.fill(BLACK)
            for j in self.laby.get_contiguous_cells(i):
                if j not in self.laby.cells[i]:

                    if j == (i[0], i[1]-1):
                        rect = pygame.Rect(0, 0, s.get_width()+4, 4)
                        pygame.draw.rect(s, WHITE, rect)

                    elif j == (i[0]+1, i[1]):
                        rect = pygame.Rect(0, s.get_height(), s.get_width()+4, 4)
                        pygame.draw.rect(s, WHITE, rect)

                    elif j == (i[0]-1, i[1]):
                        rect = pygame.Rect(0, 0, 4, s.get_height()+4)
                        pygame.draw.rect(s, WHITE, rect)

                    elif j == (i[0], i[1]+1):
                        rect = pygame.Rect(s.get_width(), 0, 4, s.get_height()+4)
                        pygame.draw.rect(s, WHITE, rect)
            if i == (self.taille-1, self.taille-1):
                image = pygame.image.load("images/image_processing20200510-8902-odjy03.png")
                image = pygame.transform.scale(image, (self.surface.height//self.taille -4,self.surface.width//self.taille -4))
                s.blit(image, (0, 0))

            surface.blit(s,
                (i[0]*(self.surface.get_height()//self.taille),
                  i[1]*(self.surface.get_height()//self.taille)))
            pygame.display.update()
        return surface

    def len_solve_dfs(self, D, A):
        pile = [D]
        pile.append(D)
        cell_marques = []
        dict_pred = {}
        dict_pred[D] = D
        cell_A_trouve = False

        while len(cell_marques) < self.taille ** 2 and cell_A_trouve == False:
            c = pile.pop(0)
            if c == A:
                cell_A_trouve = True
            else:
                voisines_c = self.laby.get_reachable_cells(c)
                for l in range(len(voisines_c)):
                    if voisines_c[l] not in cell_marques:
                        cell_marques.append(voisines_c[l])
                        pile.insert(0, voisines_c[l])
                        dict_pred[voisines_c[l]] = c

        c = A
        chemin = []
        while c != D:
            chemin.append(c)
            c = dict_pred[c]
        chemin.append(D)

        return len(chemin)