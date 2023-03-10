from random import *

class Maze:
    """
    Classe Labyrinthe
    Représentation sous forme de graphe non-orienté
    dont chaque sommet est une cellule (un tuple (l,c))
    et dont la structure est représentée par un dictionnaire
      - clés : sommets
      - valeurs : ensemble des sommets voisins accessibles
    """

    def __init__(self, height, width, empty=False):
        """
        Constructeur d'un labyrinthe de height cellules de haut
        et de width cellules de large
        Les voisinages sont initialisés à des ensembles vides
        Remarque : dans le labyrinthe créé, chaque cellule est complètement emmurée
        """
        self.height = height
        self.width = width
        self.neighbors = dict()

        if empty:
            for i in range(height):
                for j in range(width):
                    coord = []
                    if i - 1 >= 0:
                        coord.append((i - 1, j))
                    if j - 1 >= 0:
                        coord.append((i, j - 1))
                    if j + 1 < width:
                        coord.append((i, j + 1))
                    if i + 1 < height:
                        coord.append((i + 1, j))
                    self.neighbors[(i, j)] = (set(coord))
        else:
            self.neighbors = {(i, j): set() for i in range(height) for j in range(width)}

    def info(self):
        """
        **NE PAS MODIFIER CETTE MÉTHODE**
        Affichage des attributs d'un objet 'Maze' (fonction utile pour deboguer)
        Retour:
            chaîne (string): description textuelle des attributs de l'objet
        """
        txt = "**Informations sur le labyrinthe**\n"
        txt += f"- Dimensions de la grille : {self.height} x {self.width}\n"
        txt += "- Voisinages :\n"
        txt += str(self.neighbors) + "\n"
        valid = True
        for c1 in {(i, j) for i in range(self.height) for j in range(self.width)}:
            for c2 in self.neighbors[c1]:
                if c1 not in self.neighbors[c2]:
                    valid = False
                    break
            else:
                continue
            break
        txt += "- Structure cohérente\n" if valid else f"- Structure incohérente : {c1} X {c2}\n"
        return txt

    def __str__(self):
        """
        Représentation textuelle d'un objet Maze (en utilisant des caractères ascii)
        Retour:
             chaîne (str) : chaîne de caractères représentant le labyrinthe
        """
        txt = ""
        # Première ligne
        txt += "┏"
        for j in range(self.width - 1):
            txt += "━━━┳"
        txt += "━━━┓\n"
        txt += "┃"
        for j in range(self.width - 1):
            txt += "   ┃" if (0, j + 1) not in self.neighbors[(0, j)] else "    "
        txt += "   ┃\n"
        # Lignes normales
        for i in range(self.height - 1):
            txt += "┣"
            for j in range(self.width - 1):
                txt += "━━━╋" if (i + 1, j) not in self.neighbors[(i, j)] else "   ╋"
            txt += "━━━┫\n" if (i + 1, self.width - 1) not in self.neighbors[(i, self.width - 1)] else "   ┫\n"
            txt += "┃"
            for j in range(self.width):
                txt += "   ┃" if (i + 1, j + 1) not in self.neighbors[(i + 1, j)] else "    "
            txt += "\n"
        # Bas du tableau
        txt += "┗"
        for i in range(self.width - 1):
            txt += "━━━┻"
        txt += "━━━┛\n"

        return txt

    '''
    Méthode permetant d'ajouter un mur au labyrinthe entre la coordonnée c1 et c2 (supprime c1 des voisins de c2
    et c2 des voisins de c1)
    '''

    def add_wall(self, c1, c2):
        # Facultatif : on teste si les sommets sont bien dans le labyrinthe
        assert 0 <= c1[0] < self.height and \
               0 <= c1[1] < self.width and \
               0 <= c2[0] < self.height and \
               0 <= c2[1] < self.width, \
            f"Erreur lors de l'ajout d'un mur entre {c1} et {c2} : les coordonnées de sont pas compatibles avec les dimensions du labyrinthe"
        # Ajout du mur
        if c2 in self.neighbors[c1]:  # Si c2 est dans les voisines de c1
            self.neighbors[c1].remove(c2)  # on le retire
        if c1 in self.neighbors[c2]:  # Si c3 est dans les voisines de c2
            self.neighbors[c2].remove(c1)  # on le retire

    '''
    Méthode permetant de supprimer le mur entre la coordonnée c1 et c2 du labyrinthe (ajoute c1 aux voisins de c2
    et c2 aux voisins de c1)
    '''

    def remove_wall(self, c1, c2):
        assert 0 <= c1[0] < self.height and \
               0 <= c1[1] < self.width and \
               0 <= c2[0] < self.height and \
               0 <= c2[1] < self.width, \
            f"Erreur lors de la suppression d'un mur entre {c1} et {c2} : les coordonnées de sont pas compatibles avec les dimensions du labyrinthe"
        # Suppression du mur
        if c2 not in self.neighbors[c1]:  # Si c2 n'est pas dans les voisines de c1
            self.neighbors[c1].add(c2)  # on l'ajoute
        if c1 not in self.neighbors[c2]:  # Si c3 n'est pas dans les voisines de c2
            self.neighbors[c2].add(c1)  # on l'ajoute

    '''
    Methode retournant l'ensemble des murs du labyrinthe sous forme de liste de liste contenant
    les deux coordonnées voisines du mur sous forme de tuple
    Retour : Liste de liste contenant les deux coordonnées voisines du mur sous forme de tuple
    '''

    def get_walls(self):
        walls = []
        for i in range(self.height):  # Parcourt les lignes
            for j in range(self.width):  # Parcourt les colonnes
                if i - 1 > 0 and i - 1 < self.height:  # Si la cellule du dessus est dans les dimensions du labyrinthe
                    if (i - 1, j) not in self.neighbors[(i, j)]:  # Si la cellule n'est pas une voisine
                        walls.append([(i, j), (i - 1, j)])  # Ajouter à la liste des murs
                if i + 1 > 0 and i + 1 < self.height:  # Si la cellule du dessous est dans les dimensions du labyrinthe
                    if (i + 1, j) not in self.neighbors[(i, j)]:  # Si la cellule n'est pas une voisine
                        walls.append([(i, j), (i + 1, j)])  # Ajouter à la liste des murs
                if j - 1 > 0 and j - 1 < self.width:  # Si la cellule à gauche est dans les dimensions du labyrinthe
                    if (i, j - 1) not in self.neighbors[(i, j)]:  # Si la cellule n'est pas une voisine
                        walls.append([(i, j), (i, j - 1)])  # Ajouter à la liste des murs
                if j + 1 > 0 and j + 1 < self.width:  # Si la cellule à droite est dans les dimensions du labyrinthe
                    if (i, j + 1) not in self.neighbors[(i, j)]:  # Si la cellule n'est pas une voisine
                        walls.append([(i, j), (i, j + 1)])  # Ajouter à la liste des murs
        return walls  # Liste des murs sous forme d'un tuple (cellule1,cellule2) des cellules qu'il sépare '''

    '''
    Méthode transformant le labyrinthe en un labyrinthe plein (Toutes les cellules sont entourés de murs)
    Assigne a chaque cellule du labyrinthe un ensemble vide de cellules contigues.

    '''

    def fill(self):
        self.neighbors = {(i, j): set() for i in range(self.height) for j in range(self.width)}

    '''
    Méthode transformant le labyrinthe en un labyrinthe Vide (Toutes les cellules sont entourés d'aucuns murs
    (sauf les cellules sur les côtés))
    Assigne a chaque cellule du labyrinthe un ensemble contenant les coordonnées des cellules contigues.

    '''

    def empty(self):
        for i in range(self.height):
            for j in range(self.width):
                coord = []
                if i - 1 >= 0:
                    coord.append((i - 1, j))
                if j - 1 >= 0:
                    coord.append((i, j - 1))
                if j + 1 < self.width:
                    coord.append((i, j + 1))
                if i + 1 < self.height:
                    coord.append((i + 1, j))
                self.neighbors[(i, j)] = (set(coord))

    '''
    Méthode retournant une liste contenant les cellules voisines (contigues ou non)
    de la cellule placé a la coordonnée passée en paramètre
    Paramètre:
        c = coordonnée de la cellule a tester
    Retour:
        Liste contenant les cellules voisines de la cellule passée en paramètre
    '''

    def get_contiguous_cells(self, c):
        cells = []
        if c[0] - 1 >= 0:  # Si la cellule du dessus est dans les dimensions du labyrinthe
            cells.append((c[0] - 1, c[1]))

        if c[0] + 1 < self.height:  # Si la cellule du dessous est dans les dimensions du labyrinthe
            cells.append((c[0] + 1, c[1]))

        if c[1] - 1 >= 0:  # Si la cellule à gauche est dans les dimensions du labyrinthe
            cells.append((c[0], c[1] - 1))

        if c[1] + 1 < self.width:  # Si la cellule à droite est dans les dimensions du labyrinthe
            cells.append((c[0], c[1] + 1))
        return cells

    '''
    Méthode retournant une liste contenant les cellules contigues
    de la cellule placée a la coordonnée passée en paramètre
    Paramètre:
        c = coordonnée de la cellule a tester
    Retour:
        Liste contenant les cellules contigues de la cellule passée en paramètre
    '''

    def get_reachable_cells(self, c):
        accessibles = []
        voisines = self.get_contiguous_cells(c)
        for i in range(len(voisines)):
            if voisines[i] in self.neighbors[c]:
                accessibles.append(voisines[i])
        return accessibles

    """
    Génère un labyrinthe. Pour chaque cellule du labyrinthe:
        Casse le mur est ou le mur sud.
        Si la cellule ne possède qu'un de ces murs, le mur est cassé
        Si la cellule ne possède aucun de ces murs, ne rien faire
    """

    @classmethod
    def gen_btree(cls, h, w):
        L = cls(h, w, False)  # Crée un labyrinthe plein
        for i in range(h):  # Parcourt les lignes
            for j in range(w):  # parcourt les colonnes
                changement = False
                cell_contigues = L.get_contiguous_cells((i, j))
                cell_voisines = L.get_reachable_cells((i, j))
                w_c1 = False
                w_c2 = False
                # Verifie si la cellule à un voisins non atteignable à l'est et au sud
                if (i, j + 1) in cell_contigues and (i, j + 1) not in cell_voisines:
                    w_c1 = True
                if (i + 1, j) in cell_contigues and (i + 1, j) not in cell_voisines:
                    w_c2 = True
                if w_c1 and w_c2:
                    changement = True
                    # Choisit aléatoirement 1 ou 0
                    n = randint(0, 1)
                    # Si l'entier est 1 on elève le mur sud, si l'entier est 0 on elève le mur est
                    if n == 0:
                        L.remove_wall((i, j), (i, j + 1))
                    if n == 1:
                        L.remove_wall((i, j), (i + 1, j))
                # Si la cellule n'a qu'un voisin est ou sud, on supprime le mur.
                if ((w_c1 and w_c2 == False) or (w_c2 and w_c1 == False)) and changement == False:
                    if w_c1:
                        L.remove_wall((i, j), (i, j + 1))
                    if w_c2:
                        L.remove_wall((i, j), (i + 1, j))
        return L

    """
    Génère un labyrinthe. Parcourt le labyrinthe d'ouest en est et casse aléatoirement des murs est.
        Pour chaques séquences de cellules connectés, casse un mur sud aléatoirement sur le ligne
    """

    @classmethod
    def gen_sidewinder(cls, h, w):
        L = cls(h, w, False)
        for i in range(h - 1):  # Parcourt les lignes
            seq = []
            for j in range(w - 1):  # Parcourt les colonnes
                seq.append((i, j))
                n_pf = randint(0, 1)
                if n_pf == 0:
                    L.remove_wall((i, j), (i, j + 1))
                if n_pf == 1:
                    n_seq = randint(0, len(seq) - 1)
                    L.remove_wall((seq[n_seq]), (i + 1, seq[n_seq][1]))
                    seq = []
            seq.append((i, j + 1))
            n_seq = randint(0, len(seq) - 1)
            L.remove_wall((seq[n_seq]), (i + 1, seq[n_seq][1]))
        for l in range(w - 1):
            L.remove_wall((h - 1, l), (h - 1, l + 1))
        return L

    """
    Génère un labyrinthe et casse des murs aléatoirement en évitant les cycles
    """

    @classmethod
    def gen_fusion(cls, h, w):
        L = cls(h, w, False)
        D = dict()
        liste_murs = L.get_walls()
        shuffle(liste_murs)
        for i in range(h):
            for j in range(w):
                D[(i, j)] = i * w + j + 1
        for l in range(len(liste_murs)):
            if D[liste_murs[l][0]] != D[liste_murs[l][1]]:
                L.remove_wall(liste_murs[l][0], liste_murs[l][1])
                val_cell_1 = D[liste_murs[l][0]]
                D[liste_murs[l][0]] = D[liste_murs[l][1]]
                for cle, valeur in D.items():
                    if valeur == val_cell_1:
                        D[cle] = D[liste_murs[l][0]]
        return L

    """
   Génère un labyrinthe en l'expolrant et en cassant les murs que l'on rencontre
   """

    @classmethod
    def gen_exploration(cls, h, w):
        # Initialisation
        L = cls(h, w, False)
        visited = list()
        depart = (randint(0, h - 1), randint(0, w - 1))
        pile = [depart]
        visited.append(depart)
        # Tant que la pile n'est pas vide
        while pile:
            continuer = True
            # La position devient la dernière cellule de la pile et la supprime de la pile
            position = pile.pop()
            voisins = list(L.get_contiguous_cells(position))
            shuffle(voisins)
            i = 0
            while i < len(voisins) and continuer == True:
                # Vérifie si cette cellule a des voisins non visités
                if voisins[i] not in visited:
                    # On ajout le position à la pile
                    pile.append(position)
                    # On casse le mur
                    L.remove_wall(position, voisins[i])
                    # On ajoute la cellule à la pile et aux cellules visités
                    visited.append(voisins[i])
                    pile.append(voisins[i])
                    continuer = False
                i += 1
        return L


    """
    Génère un labyrinthe avec des marches aléatoires jusqu'à l'obtention d'une arborescence 
    """
    @classmethod
    def gen_wilson(cls, h, w):
        # Initialisation
        L = cls(h, w, False)
        depart = (randint(0, h - 1), randint(0, w - 1))
        marque = [depart]
        # tant que toutes les cellules ne sont pas marqués
        while len(marque) < h * w:
            # Choisit une position aléatoire non marquée
            position = (randint(0, h - 1), randint(0, w - 1))
            while position in marque:
                position = (randint(0, h - 1), randint(0, w - 1))
            chemin = [position]
            # tant que la position n'est pas marquée
            while position not in marque:
                voisins = L.get_contiguous_cells(position)
                cible = choice(voisins)
                # Si la cible (position que l'on souhaite atteindre) est dans le chemin
                if cible in chemin:
                    idx = 0
                    continuer = True
                    while idx < len(chemin) and continuer == True:
                        # Récupération de l'occurence de la cible dans le chemin
                        if chemin[idx] == cible:
                            continuer = False
                            idx -= 1
                        idx += 1
                    nouveau_chemin = []
                    # Création d'un nouveau chemin du début jusqu'à la première ocurence de la cible
                    for i in range(idx + 1):
                        nouveau_chemin.append(chemin[i])
                    chemin = nouveau_chemin
                    position = chemin[-1]
                # Sinon on se déplace sur cible et on l'ajoute au chemin
                else:
                    position = cible
                    chemin.append(position)
            # Si la position est marquée, on marque le chemin et on casse les murs
            if position in marque:
                test_m = []
                for i in range(len(chemin) - 1):
                    test_m.append(chemin[i])
                    L.remove_wall(chemin[i], chemin[i + 1])
                    if chemin[i] not in marque:
                        marque.append(chemin[i])
                if chemin[-1] not in marque:
                    marque.append(chemin[-1])

        return L



def overlay(self, content=None):
    """
    Rendu en mode texte, sur la sortie standard, \
    d'un labyrinthe avec du contenu dans les cellules
    Argument:
        content (dict) : dictionnaire tq content[cell] contient le caractère à afficher au milieu de la cellule
    Retour:
        string
    """
    if content is None:
        content = {(i, j): ' ' for i in range(self.height) for j in range(self.width)}
    else:
        # Python >=3.9
        # content = content | {(i, j): ' ' for i in range(
        #    self.height) for j in range(self.width) if (i,j) not in content}
        # Python <3.9
        new_content = {(i, j): ' ' for i in range(self.height) for j in range(self.width) if (i, j) not in content}
        content = {**content, **new_content}
    txt = r""
    # Première ligne
    txt += "┏"
    for j in range(self.width - 1):
        txt += "━━━┳"
    txt += "━━━┓\n"
    txt += "┃"
    for j in range(self.width - 1):
        txt += " " + content[(0, j)] + " ┃" if (0, j + 1) not in self.neighbors[(0, j)] else " " + content[
            (0, j)] + "  "
    txt += " " + content[(0, self.width - 1)] + " ┃\n"
    # Lignes normales
    for i in range(self.height - 1):
        txt += "┣"
        for j in range(self.width - 1):
            txt += "━━━╋" if (i + 1, j) not in self.neighbors[(i, j)] else "   ╋"
        txt += "━━━┫\n" if (i + 1, self.width - 1) not in self.neighbors[(i, self.width - 1)] else "   ┫\n"
        txt += "┃"
        for j in range(self.width):
            txt += " " + content[(i + 1, j)] + " ┃" if (i + 1, j + 1) not in self.neighbors[(i + 1, j)] else " " + \
                                                                                                             content[(
                                                                                                             i + 1,
                                                                                                             j)] + "  "
        txt += "\n"
    # Bas du tableau
    txt += "┗"
    for i in range(self.width - 1):
        txt += "━━━┻"
    txt += "━━━┛\n"
    return txt


def solve_dfs(self, D, A):
    pile = [D]
    pile.append(D)
    cell_marques = []
    dict_pred = {}
    dict_pred[D] = D
    cell_A_trouve = False

    while len(cell_marques) < self.height * self.width and cell_A_trouve == False:
        c = pile.pop(0)
        if c == A:
            cell_A_trouve = True
        else:
            voisines_c = self.get_reachable_cells(c)
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

    return chemin


def solve_bfs(self, D, A):
    file = [D]
    file.append(D)
    cell_marques = []
    dict_pred = {}
    dict_pred[D] = D
    cell_A_trouve = False
    while len(cell_marques) < self.height * self.width and cell_A_trouve == False:
        c = file.pop()
        if c == A:
            cell_A_trouve = True
        else:
            voisines_c = self.get_reachable_cells(c)
            for l in range(len(voisines_c)):
                if voisines_c[l] not in cell_marques:
                    cell_marques.append(voisines_c[l])
                    file.append(voisines_c[l])
                    dict_pred[voisines_c[l]] = c
    c = A
    chemin = []
    while c != D:
        chemin.append(c)
        c = dict_pred[c]
    chemin.append(D)

    return chemin


def solve_rhr(self, D, A):
    direction = "Droite"
    position = D
    cases_visites = [D]
    i = 0
    while position != A:
        mouvement = False
        if direction == "Droite" and mouvement == False:
            if (position[0] + 1, position[1]) in self.get_reachable_cells(position):
                cases_visites.append((position[0] + 1, position[1]))
                position = (position[0] + 1, position[1])
                mouvement = True
                direction = "Bas"
            else:
                if (position[0], position[1] + 1) in self.get_reachable_cells(position):
                    cases_visites.append((position[0], position[1] + 1))
                    position = (position[0], position[1] + 1)
                    mouvement = True
                else:
                    direction = "Haut"

        if direction == "Haut" and mouvement == False:
            if (position[0], position[1] + 1) in self.get_reachable_cells(position):
                cases_visites.append((position[0], position[1] + 1))
                position = (position[0], position[1] + 1)
                mouvement = True
                direction = "Droite"
            else:
                if (position[0] - 1, position[1]) in self.get_reachable_cells(position):
                    cases_visites.append((position[0] - 1, position[1]))
                    position = (position[0] - 1, position[1])
                    mouvement = True
                else:
                    direction = "Gauche"

        if direction == "Gauche" and mouvement == False:
            if (position[0] - 1, position[1]) in self.get_reachable_cells(position):
                cases_visites.append((position[0] - 1, position[1]))
                position = (position[0] - 1, position[1])
                mouvement = True
                direction = "Haut"
            else:
                if (position[0], position[1] - 1) in self.get_reachable_cells(position):
                    cases_visites.append((position[0], position[1] - 1))
                    position = (position[0], position[1] - 1)
                    mouvement = True
                else:
                    direction = "Bas"

        if direction == "Bas" and mouvement == False:
            if (position[0], position[1] - 1) in self.get_reachable_cells(position):
                cases_visites.append((position[0], position[1] - 1))
                position = (position[0], position[1] - 1)
                mouvement = True
                direction = "Gauche"
            else:
                if (position[0] + 1, position[1]) in self.get_reachable_cells(position):
                    cases_visites.append((position[0] + 1, position[1]))
                    position = (position[0] + 1, position[1])
                    mouvement = True
                else:
                    direction = "Droite"
    return cases_visites


"""Calcule la distance géostatique entre c1 et c2"""


def distance_geo(self, c1, c2):
    return len(self.solve_dfs(c1, c2)) - 1


"""Calcule la distance de manhattan entre c1 et c2"""


def distance_man(self, c1, c2):
    return abs(c2[0] - c1[0]) + abs(c2[1] - c1[1])