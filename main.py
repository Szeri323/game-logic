from getpass import getpass
from authentication import authentication
from data_manager import pick_character, match_character_with_acoount, write_json
from game import game

def main():
    login = str(input("Write your login: "))
    password = str(getpass("Write your password: "))
    if authentication(login, password):
        character = pick_character(login)
        game(character)
        accounts = match_character_with_acoount(login, character)
        write_json(accounts)
    else:
        print("Access deneid. Wrong login or password. Please try agin.")
    
main()