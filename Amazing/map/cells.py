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
        print(self.cells)
        print(test)
