  
def print_message(message, communicate_type = "", character = ""):
    if communicate_type == "system":
        print('@'*20)
        print(message)
        print('@'*20)
    elif communicate_type == "game":
        print('-'*20)
        print(message)
        print('-'*20)
    elif communicate_type == "dialog" and character != "":
        print('-'*20)
        print(f'{character}: {message}')
        print('-'*20)
    else:
        print(' '*20)
        print(message)
        print(' '*20)