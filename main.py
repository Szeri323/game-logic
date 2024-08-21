from getpass import getpass
from authentication import authentication
from data_manager import pick_character
from game import game

def main():
    login = str(input("Write your login: "))
    password = str(getpass("Write your password: "))
    if authentication(login, password):
        character = pick_character(login)
        game(character)
    else:
        print("Access deneid. Wrong login or password. Please try agin.")
    
main()