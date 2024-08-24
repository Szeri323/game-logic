#from user_accounts import accounts
import json


def read_json():
    with open('accounts.json') as f:
        return json.load(f)
def write_json(data):
    with open('accounts.json', "w") as o:
        json.dump(data, o)

def match_character_with_acoount(login, character):
    try:
        accounts = read_json()
        if len(accounts[login]["characters"]) != 0:
            for i in range(len(accounts[login]["characters"])):
                if character["nick"] == accounts[login]["characters"][i]["nick"]:
                    accounts[login]["characters"][i] = character
                else:
                    accounts[login]["characters"].append(character)
        else:
            accounts[login]["characters"].append(character)  
        return accounts
    except KeyError:
        return None    

def get_account_credentials(login):
    """Get accounts credentials
    
    :param login: str - login which we are looking for login details
    :return: str,str - account credentials.
    
    """
    try: 
        accounts = read_json()
        if accounts[login]:
            return accounts[login]["login"], accounts[login]["password"]
    except KeyError:
        return None

def pick_character(login):
    """Pick character or create one.
    
    :param login: str - specifier for resources.
    :return: dict - one choosen character which we want to play.
    
    """
    accounts = read_json()
    user_characters = accounts[login]["characters"]
    if len(user_characters) == 0:
        user_characters = create_character(user_characters) 
    return user_characters[choose_character(user_characters)]

def create_character(user_characters):
    """Create new character
    
    :param user_characters: list - list of characters
    :return: list - update list of characters
    
    """
    nick = str(input("Choose your characters nick: "))
    character = {
        "nick": nick,
        "level": 1,
        "statistics": {"vitality": 5, "strength": 5, "intelligence": 5, "agility": 5},
        "money": 0,
        "equpiement": [],
        "gear": {
            "head": 0,
            "neck": 0,
            "torso": 0,
            "left_hend": 0,
            "right_hand": 0,
            "legs": 0
        }
    }
    
    user_characters.append(character)
    return user_characters
    
def choose_character(user_characters):
    """Choose character from list
    
    :param user_characters: list - list of characters.
    :return: int - index of choosen character.
    
    """
    [print(i) for i in range(len(user_characters))]
    return int(input(f"Choose your character from 0 to {len(user_characters)-1}: "))
    