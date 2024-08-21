from communicates import print_message
from graphics import show_map

Player = {"symbol": "P", "position": (0,0)}
Forgerer = {"symbol": "F", "position": (1,1)}
Rock = {"symbol": "r", "position": (3,3)}
npcs = [Player, Forgerer, Rock]

def game(character):
    """This main game loop.
    
    :param character: dict - all data about choosen character.
    :return: None - ends game. 
    
    """
    message = """Game start\nWrite one of above commands:\n show [nick, level, money, eq, gear] - to show choosen parameter,\n money - to check how much money you have,\n exp - to gain expirience and find gear,\n job - to earn."""
    print_message(message, "system")
    print_message(f"Hello {character['nick']}, big adventur is wating for you.", "game")
    try:
        while True:
            new_map = init_map("city_map")
            set_on_map(new_map, npcs)
            show_map(new_map)
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
                    set_player_position(x, y)
    #implement mod - if player coordinates meet with npc run defined mod (fight, quest, trade, mine) 
            
    except KeyboardInterrupt:
        return 
    
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
        
def set_player_position(x, y):
    """Takes coordinates and sets player position
    
    :param x: int - Players x position
    :param y: int - Players y position
    :return: None - Set players coordinates
    
    """
    Player["position"] = (x, y)
    
def set_on_map(new_map, npcs):
    for npc in npcs:
        new_map[npc["position"][0]][npc["position"][1]] = npc["symbol"]
        