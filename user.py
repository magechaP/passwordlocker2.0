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