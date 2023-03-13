import pygame

import Amazing.Const


class Cells:
    def __int__(self, surface, nb_cells):

        self.surface = surface
        """self.height = height
        self.width = width"""
        self.nb_cells = nb_cells

    def create(self):
        pair = 2
        dict = []
        for i in range(0, self.surface.get_height() + 1, self.surface.get_height() // self.nb_cells):
            for j in range(0, self.surface.get_height() + 1, self.surface.get_height() // self.nb_cells):
                pygame.display.flip()
                if pair % 2 == 0:
                    pygame.Surface((self.surface.get_height(),
                                    self.surface.get_width()),)

                    print(f"pair{(i, j)}")
                else:
                    pygame.draw.rect(self.surface, Amazing.Const.BLACK, (i, j, 40, 40))
                    print(f"impair {(i, j)}")
                pair += 1
            pair -= 1
