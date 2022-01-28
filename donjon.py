import numpy as np


def donjon():
    return ([8*'-' + 4*' ' + 7*'-',
    '|' + 6*'.' + '|' + 2*' ' + 2*'#' + '+' + 5*'.' + '|',
    '|' + 6*'.' + '|' + 2*' ' + '# |' + 5*'.' + '|',
    '|' + 6*'.' + '+### |' + 5*'.' + '|',
    8*'-' + 4*' ' + 7*'-'])

# var globales :
SHAPE = (20,20)


# définition donjon, salles, couloirs :
class Donjon:
    """ Renvoie la matrice avec des +, -, # etc quand on fait donjon = str(Donjon(arguments))
    (je m'occuperai de définir les arguments si vous voulez)

    Args :
        


    Attributes :
        salles (list): liste des salles et couloirs (qui sont des instances de Room ou de Corridor)
    

    """
    def __init__(self, salles):
        self.salles = salles
        #
    
    def __str__(self):
        matrix = ' ' * np.ones(SHAPE, dtype = object)
        for salle in self.salles :
            if isinstance(salle, Room):
                tlc, drc = salle.top_left_corner(), salle.down_right_corner()
                matrix[tlc[0]: drc[0], tlc[1]: drc[1]] = str(salle)
            elif isinstance(salle, Corridor):
                direction = salle.direction
                e, l = salle.entry, salle.length
                if direction == 'h':
                    matrix[e[0], e[0] + l] = str(salle)
                else :
                    matrix[:, e[1]: e[1] + l] = str(salle)
        return matrix



class Room:
    """salles 
    
    att : 
        corner : coin haut gauche
        length, width : définit la forme de la salle
        content (list) : list of objects/ characters and their position in the room
    """
    def __init__(self, corner, length, width, content=[]):
        self.length = length
        self.width = width
        self.content = content
        self.corner = corner
    
    def top_left_corner(self):
        return self.corner
    
    def down_right_corner(self):
        return self.corner[0] + self.length -1 , self.corner[1] + self.width -1

    def __str__(self):
        matrix = '.' * np.ones((self.length, self.width), dtype = object)
        matrix[:, 0], matrix[:, -1] = '|', '|'
        matrix[0, :], matrix[-1, :] = '-', '-'
        # il reste à ajouter les portes et les objets qui sont ds la salle
        return matrix



class Corridor:
    """couloirs
    attributs : longueur, point de départ et direction (vertical/ horizontal) 
    
    """
    def __init__(self, entry, length, direction='h'):
        self.entry = entry
        self.direction = direction
        self.length = length
    
    def __str__(self):
        m = '#' * np.ones((self.length), dtype = object)
        if self.direction == 'h':
            return m
        else :
            return m.T


# tester Donjon avec les arguments :
ARGS = [Room(corner = (0,0), length = 8, width = 8), Room((0,13), 7, 7), Room((8,21), 4, 6),
Corridor(entry = (3,9), length = 3), Corridor((2,9), 1), Corridor((1,9), 2), 
Corridor((3,19), 8), Corridor((3,26), 3, 'v'), Corridor((6,23), 4), Corridor((7, 23), 1)]

