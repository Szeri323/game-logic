from data_manager import get_account_credentials

def authentication(login, password):
    """Checks if login and password match with acounts credentials
    
    :param login: str - string with user login passed by user
    :param password: str - string with user password passed by user
    :return: bool - result of authentication
    
    """
    try:
        account_login, account_password = get_account_credentials(login)
        if login == account_login and password == account_password:
                return True
    except TypeError:
        return False
