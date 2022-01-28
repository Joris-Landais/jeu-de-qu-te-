# personnages et objets :

class Character:
    """ main character (= perso principal = nous) + PNJs (mechants et marchands)
    
    Args:
    
    Attributes:
        role (str): mc / enemy / merchant
        bag (list): 
        life (dict) :

    """
    def __init__(self, life,strength):
        self.life=life
        self.strength=strength
    def up_grade_strength():
        self.strength+=1
    def fight(strength):
        self.life-=strength
        
class main_Character(Character):
    def __init__(self, bag:dict, life, monney):
        super().__init__(id, life, strength)
        self.bag=bag
        self.monney=0
    def found_monney ():
        monney+=1
