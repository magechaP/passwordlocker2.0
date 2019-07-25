class User:
    """
    Class that generates new instances of users   
    """

    users = []

    def __init__(self,name,login_password):
        """
        Initialization method that enables us to define properties for our objects
        Args:
        name: Account username for new user
        login_password: Account password for new user
        """
        self. name = name
        self.login_password = login_password

    def save_user(self):
        """
        save_user method that helps a user create an account with password locker
        """
        User.users.append(self)

    @classmethod
    def display_all(cls):
        """
        display_all method that helps user view their account details
        """
        return cls.users