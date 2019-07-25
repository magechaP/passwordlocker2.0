import pyperclip      #importing pyperclip module

class Credential:
    """
    Class that generates new instances of credentials
    """
    
    credentials = []

    def __init__(self, username, accountname, password,):
        """
        __init__ method that enables us to define properties for our objects
        Args:
        username: Username for an account being added
        accountname: Name of the account being added
        password: Password for the account being added
        """
        self.username = username
        self.accountname = accountname
        self.password = password

    def save_credential(self):
        """
        save_credential method to help a user save a credential
        """
        Credential.credentials.append(self)

    def delete_credential(self):
        """
        delete_method to help a user delete an existing credential
        """
        Credential.credentials.remove(self)        