from entity import Entity

class Enemy(Entity):
    
    def __init__(self, symbol, position, health, attack):
        super().__init__(symbol, position)
        self.health = health
        self.attack = attack