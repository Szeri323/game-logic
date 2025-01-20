class Player:
    nick = ""
    symbol = "P"
    position = (0, 0)
    level = 1
    health = 5
    attack = 5
    #statistics
    statistics = {"vitality": 5, "strength": 5, "intelligence": 5, "agility": 5} 
    equipement = [] 
    money = 0 
    gear = {"head": 0, "neck": 0, "torso": 0, "left_hend": 0, "right_hand": 0, "legs": 0}
    
print(Player.statistics["vitality"])