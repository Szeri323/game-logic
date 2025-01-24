from communicates import print_message
from graphics import show_map, show_player_statistics
from keyboard_listener import getkey
import os

    # implement commands, show P after won fight, back P to last position if lost
    # implement quests and color if npc has quest
    # implement spawner and enemys that spawner creates

# Message types:
system = "system"
game = "game"
dialog = "dialog"

Player = {"symbol": "P", "position": (0,0)}
Ranger = {"symbol": "R", "quest": True, "position": (0,9)}
Spawner = {"symbol": "S", "position": (6,6)}
Forgerer = {"symbol": "F", "position": (1,1)}
Enemy = {"symbol": "E", "statistics": {"vitality": 2, "strength": 2}, "position": (2,2)}
Rock = {"symbol": "r", "position": (3,3)}
npcs = [Player, Ranger, Spawner, Forgerer, Enemy, Rock]

def comand_check(command):
    """Checks if the command is correct.
    
    :param command: str - command to check.
    :return: bool - return True if command is correct, False otherwise.
    
    """
    commands = ['show', 'exp', 'job', 'move']
    if command in commands:
        return True
    return False

def init_map(type_of_map, x, y):
    world_map = []
    if type_of_map == "city_map":
        for i in range(x):
            world_map.append([])
            for _ in range(y):
                world_map[i].append(" ")
    return world_map
            
        
def set_player_position(x, y, new_map):
    """Takes coordinates and sets player position
    
    :param x: int - Players x position
    :param y: int - Players y position
    :return: None - Set players coordinates
    
    """
    old_position = Player["position"]
    Player["position"] = (x, y)
    new_map[old_position[0]][old_position[1]] = " "
    new_map[Player["position"][0]][Player["position"][1]] = Player["symbol"]
    
def set_on_map(new_map, npcs):
    for npc in npcs:
        new_map[npc["position"][0]][npc["position"][1]] = npc["symbol"]

def call_event(npc, character):
    if npc["symbol"] == "F":
        print_message("Hello adventurer, how can I help you?", dialog, "Forgerer")
        choice = str(input("upgrade or trade:"))
        if choice == "upgrade":
            upgrade()
            return True
        if choice == "trade":
            trade()
            return True
        else:
            print("Wrong option.")
            return False
    if npc["symbol"] == "E":
        if fight(character, "E"):
            Enemy = None
            character["level"] += 1
            character["money"] += 2
            print_message("Fight won.", game)
            return True
        else:
            print_message("Fight lost.", game)
            return False
    if npc["symbol"] == "S":
        if fight(character, "S"):
            Enemy = None
            character["level"] += 1
            character["money"] += 2
            print_message("Fight won.", game)
            return True
        else:
            print_message("Fight lost.", game)
            return False
    else:
        return False

def trade():
    print("Trade complete.")
    
def upgrade():
    print("Upgrade complete.")
    
def fight(character, enemy_type):
    if enemy_type == "E":
        player_value = character["statistics"]["vitality"] + character["statistics"]["strength"]
        enemy_value = Enemy["statistics"]["vitality"] + Enemy["statistics"]["strength"]
        if player_value > enemy_value:
            return True
        else:
            return False
    if enemy_type == "S":
        npcs.append({"symbol": "E", "statistics": {"vitality": 2, "strength": 2}, "position": (8,15)})
        npcs.append(Enemy)
        npcs.append(Enemy)
        npcs.append(Enemy)
        print(npcs)
    


def game(character):
    """This main game loop.
    
    :param character: dict - all data about choosen character.
    :return: None - ends game. 
    
    """
    new_map = init_map("city_map", 10, 20)
    message = """Game start\nWrite one of above commands:\n show [nick, level, money, eq, gear] - to show choosen parameter,\n money - to check how much money you have,\n exp - to gain expirience and find gear,\n job - to earn."""
    print_message(message, system)
    print_message(f"Hello {character['nick']}, big adventur is wating for you.", game)
    try:
        while True:
            
            messages = []
            
            set_on_map(new_map, npcs)
            show_player_statistics(character)
            show_map(new_map)
            
            k = getkey()
                
            os.system('clear')
            if k == 'esc':
                quit()
            else:
                if k in ['w', 's', 'a', 'd']:
                    x, y = Player["position"]
                    # print(x, y)
                    if k == 'w' and x > 0:
                        x-=1
                    if k == 's' and x < len(new_map[0])-1:
                        x+=1
                    if k == 'd' and y < len(new_map[0])-1:
                        y+=1
                    if k == 'a' and y > 0:
                        y-=1
                    for npc in npcs[1:]:
                            if (x, y) == npc["position"]:
                                if call_event(npc, character):
                                    set_player_position(x, y, new_map)
                                else:
                                    # print_message("Can't walk to those coordinates.", "game")
                                    messages.append(["Can't walk to those coordinates.", "game"])
                                    if k == 'w':
                                        x+=1
                                        Player["position"] = (x, y)
                                    if k == 's':
                                        x-=1
                                        Player["position"] = (x, y)
                                    if k == 'd':
                                        y-=1
                                        Player["position"] = (x, y)
                                    if k == 'a':
                                        y+=1
                                        Player["position"] = (x, y)
                                    
                            else:
                                set_player_position(x, y, new_map)
                elif k == "/":
                    command = str(input())
                    if comand_check:
                        if command == 'show':
                            param = str(input())
                            print_message(f"{param}: {character[param]}")
                        if command == 'money':
                            print_message(f"money: {character['money']}")
                        if command == 'exp':
                            character['level'] += 1
                        if command == 'job':
                            character['money'] += 5
                        if command == 'move':
                            x = int(input())
                            y = int(input())
                            
                else:
                    print("Use binded keys, if you need help click '/', write 'help' and click enter.")
                for message in messages:
                    print_message(message[0], message[1])
            
    except (KeyboardInterrupt, SystemExit):
        os.system('stty sane')
        return character
    
