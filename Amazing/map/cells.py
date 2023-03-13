import pygame
import Amazing.Const


class Cells:
    def __init__(self, surface, nb_cells):

        self.surface = surface
        self.nb_cells = nb_cells


    def create(self):
        pair = 2
        self.cells = {}
        ci = 0
        test = []
        for i in range(0, self.surface.get_height(), self.surface.get_height() // self.nb_cells):
            cj = 0
            for j in range(0, self.surface.get_height(), self.surface.get_height() // self.nb_cells):
                pygame.display.flip()
                """if pair % 2 == 0:
                    s = pygame.Surface((self.surface.get_height(),
                                        self.surface.get_width()),)
                    s.fill(Amazing.Const.WHITE)

voir si c'est utile plus tard

                    print(f"pair{(i, j)}")
                else:
                    s = pygame.Surface((self.surface.get_height(),
                                        self.surface.get_width()), )
                    s.fill(Amazing.Const.BLACK)
                    print(f"impair {(i, j)}")"""
                self.cells.update({(ci, cj): {}})
                test.append((ci, cj))
                cj += 1
            ci += 1
        return self.cells

    #A faire get_contiguous_cells qui retournera une list

    def get_contiguous_cells(self, c):
        cells = []
        if c[0] - 1 >= 0:  # Si la cellule du dessus est dans les dimensions du labyrinthe
            cells.append((c[0] - 1, c[1]))

        if c[0] + 1 < self.surface.get_height():  # Si la cellule du dessous est dans les dimensions du labyrinthe
            cells.append((c[0] + 1, c[1]))

        if c[1] - 1 >= 0:  # Si la cellule à gauche est dans les dimensions du labyrinthe
            cells.append((c[0], c[1] - 1))

        if c[1] + 1 < self.surface.get_width():  # Si la cellule à droite est dans les dimensions du labyrinthe
            cells.append((c[0], c[1] + 1))
        return cells

