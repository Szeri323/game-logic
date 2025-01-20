from entity import Entity

class Npc(Entity):
    
    def __init__(self, symbol, position, name, quest):
        super().__init__(symbol, position)
        self.name = name
        self.quest = quest