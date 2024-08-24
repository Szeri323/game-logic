from communicates import print_message
from graphics import show_map
from keyboard_listener import getkey
import os

# Message types:
system = "system"
game = "game"
dialog = "dialog"



Player = {"symbol": "P", "position": (0,0)}
Forgerer = {"symbol": "F", "position": (1,1)}
Enemy = {"symbol": "E", "position": (2,2)}
Rock = {"symbol": "r", "position": (3,3)}
npcs = [Player, Forgerer, Enemy, Rock]

def game(character):
    """This main game loop.
    
    :param character: dict - all data about choosen character.
    :return: None - ends game. 
    
    """
    new_map = init_map("city_map")
    message = """Game start\nWrite one of above commands:\n show [nick, level, money, eq, gear] - to show choosen parameter,\n money - to check how much money you have,\n exp - to gain expirience and find gear,\n job - to earn."""
    print_message(message, system)
    print_message(f"Hello {character['nick']}, big adventur is wating for you.", game)
    try:
        while True:
            
            set_on_map(new_map, npcs)
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
                                if call_event(npc):
                                    set_player_position(x, y, new_map)
                                else:
                                    print_message("Can't walk to those coordinates.", "game")
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
                else:
                    continue
            
            # command = str(input())
            # if comand_check:
            #     if command == 'show':
            #         param = str(input())
            #         print_message(f"{param}: {character[param]}")
            #     if command == 'money':
            #         print_message(f"money: {character['money']}")
            #     if command == 'exp':
            #         character['level'] += 1
            #     if command == 'job':
            #         character['money'] += 5
            #     if command == 'move':
            #         x = int(input())
            #         y = int(input())
                    
    # implement commands, show P after won fight, back P to last position if lost
            
    except (KeyboardInterrupt, SystemExit):
        return character
    
def comand_check(command):
    """Checks if the command is correct.
    
    :param command: str - command to check.
    :return: bool - return True if command is correct, False otherwise.
    
    """
    commands = ['show', 'exp', 'job', 'move']
    if command in commands:
        return True
    return False

def init_map(type_of_map):
    if type_of_map == "city_map":
        return [
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "],
        ]
        
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

def call_event(npc):
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
        fight()
        return True
    else:
        return False

def trade():
    print("Trade complete.")
def upgrade():
    print("Upgrade complete.")
def fight():
    print("Fight won.")
