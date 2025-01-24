from entity import Entity

class Player(Entity):
    def __init__(self, symbol="", position=...):
        super().__init__(symbol, position)
        self.nick = ""
        self.level = 1
        self.health = 5
        self.attack = 5
        #statistics
        self.statistics = {"vitality": 5, "strength": 5, "intelligence": 5, "agility": 5} 
        self.equipement = [] 
        self.money = 0 
        self.gear = {"head": 0, "neck": 0, "torso": 0, "left_hend": 0, "right_hand": 0, "legs": 0}
