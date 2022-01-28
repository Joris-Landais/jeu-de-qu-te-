from turtle import width
import numpy as np


def donjon():
    return ([8*'-' + 4*' ' + 7*'-',
    '|' + 6*'.' + '|' + 2*' ' + 2*'#' + '+' + 5*'.' + '|',
    '|' + 6*'.' + '|' + 2*' ' + '# |' + 5*'.' + '|',
    '|' + 6*'.' + '+### |' + 5*'.' + '|',
    8*'-' + 4*' ' + 7*'-'])

# var globales :
SHAPE = (20,20)
# tester Donjon avec les arguments :
ARGS = []


# définition donjon, salles, couloirs :
class Donjon:
    """ Renvoie la matrice avec des +, -, # etc quand on fait donjon = str(Donjon(arguments))
    (je m'occuperai de définir les arguments si vous voulez)

    Args :
        xx


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
    def __init__(self, corner, length, width, content):
        self.length = length
        self.width = width
        self.content = content
    
    def top_left_corner(self):
        return self.corner
    
    def down_right_corner(self):
        return self.corner[0] + self.length, self.corner[1] + self.width

    def __str__(self):
        matrix = '.' * np.ones((self.length, self.width), dtype = object)
        matrix[:, 0], matrix[:, -1] = '|', '|'
        matrix[0, :], matrix[-1, :] = '-', '-'
        # il reste à ajouter la porte et les objets qui sont ds la salle
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





# personnages et objets :

class Character:
    """ main character (= perso principal = nous) + PNJs (mechants et marchands)
    
    Args:
    
    Attributes:
        role (str): mc / enemy / merchant
        bag (list): 
        stats (dict) :

    """
    def __init__(self, role, bag, stats):
        pass

class Object:
    """ objets trouvés ds donjon / achetés / obtenus en battant un ennemi
    
    """
    def __init(self):
        pass
