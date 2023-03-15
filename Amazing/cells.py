import pygame


class Cells:
    def __init__(self, surface, nb_cells):

        self.surface = surface
        self.nb_cells = nb_cells

        self.cells = {}
        ci = 0
        test = []
        for i in range(0, self.surface.get_height(), self.surface.get_height() // self.nb_cells):
            cj = 0
            for j in range(0, self.surface.get_height(), self.surface.get_height() // self.nb_cells):
                pygame.display.flip()
                self.cells.update({(ci, cj): []})
                test.append((ci, cj))
                cj += 1
            ci += 1

    def get_contiguous_cells(self, c):
        cells = []
        if c[0] - 1 >= 0:  # Si la cellule du dessus est dans les dimensions du labyrinthe
            cells.append((c[0] - 1, c[1]))

        if c[0] + 1 < self.nb_cells:  # Si la cellule du dessous est dans les dimensions du labyrinthe
            cells.append((c[0] + 1, c[1]))

        if c[1] - 1 >= 0:  # Si la cellule à gauche est dans les dimensions du labyrinthe
            cells.append((c[0], c[1] - 1))

        if c[1] + 1 < self.nb_cells:  # Si la cellule à droite est dans les dimensions du labyrinthe
            cells.append((c[0], c[1] + 1))
        return cells

    def empty(self):
        for i in self.cells.keys():
            for j in self.get_contiguous_cells(i):
                self.cells[i].append(j)

    def fill(self):
        self.cells = {(i, j): [] for i in range(self.nb_cells) for j in range(self.nb_cells)}


    def add_wall(self, c1, c2):
        # Facultatif : on teste si les sommets sont bien dans le labyrinthe
        assert 0 <= c1[0] < self.surface.get_height() and \
               0 <= c1[1] < self.surface.get_width() and \
               0 <= c2[0] < self.surface.get_height() and \
               0 <= c2[1] < self.surface.get_width(), \
            f"Erreur lors de l'ajout d'un mur entre {c1} et {c2} : les coordonnées de sont pas compatibles avec les dimensions du labyrinthe"
        # Ajout du mur

        if c2 in self.cells[c1]:  # Si c2 est dans les voisines de c1
            self.cells[c1].remove(c2)  # on le retire
        if c1 in self.cells[c2]:  # Si c3 est dans les voisines de c2
            self.cells[c2].remove(c1)  # on le retire

    def remove_wall(self, c1, c2):
        # Facultatif : on teste si les sommets sont bien dans le labyrinthe
        assert 0 <= c1[0] < self.surface.get_height() and \
               0 <= c1[1] < self.surface.get_width() and \
               0 <= c2[0] < self.surface.get_height() and \
               0 <= c2[1] < self.surface.get_width(), \
            f"Erreur lors de l'ajout d'un mur entre {c1} et {c2} : les coordonnées de sont pas compatibles avec les dimensions du labyrinthe"
        # Ajout du mur

        if c2 not in self.cells[c1]:  # Si c2 est dans les voisines de c1
            self.cells[c1].append(c2)  # on le retire
        if c1 not in self.cells[c2]:  # Si c3 est dans les voisines de c2
            self.cells[c2].append(c1)  # on le retire

    def get_reachable_cells(self, c):
        accessibles = []
        voisines = self.get_contiguous_cells(c)
        for i in range(len(voisines)):
            if voisines[i] in self.cells[c]:
                accessibles.append(voisines[i])
        return accessibles
















"""    def create(self):
        pair = 2
        self.cells = {}
        ci = 0
        test = []
        for i in range(0, self.surface.get_height(), self.surface.get_height() // self.nb_cells):
            cj = 0
            for j in range(0, self.surface.get_height(), self.surface.get_height() // self.nb_cells):
                pygame.display.flip()
                self.cells.update({(ci, cj): {}})
                test.append((ci, cj))
                cj += 1
            ci += 1
        return self.cells
"""
