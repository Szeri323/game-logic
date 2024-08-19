def game(character):
    """This main game loop.
    
    :param character: dict - all data about choosen character.
    :return: None - ends game. 
    
    """
    try:
        while True:
            print(f"Hello {character['nick']}, big adventur is wating for you.")
            print(f"Write one of above commands:\n show [nick, level, money, eq, gear] - to show choosen parameter,\n exp - to gain expirience and find gear,\n job - to earn.")
            command = str(input())
            if comand_check:
                if command == 'show':
                    param = str(input())
                    print(f"{param}: {character[param]}")
                if command == 'exp':
                    character['level'] += 1
                if command == 'job':
                    character['money'] += 5
    except KeyboardInterrupt:
        return 
    
def comand_check(command):
    """Checks if the command is correct.
    
    :param command: str - command to check.
    :return: bool - return True if command is correct, False otherwise.
    
    """
    commands = ['show', 'exp', 'job']
    if command in commands:
        return True
    return False
        
