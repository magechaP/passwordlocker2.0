from user import User    #importing the unittest module
import unittest         #importing the User class

class TestUser(unittest.TestCase):
    """
    Test class that defines the test cases for the user class behaviours
    Args:
    unittest.TestCase: TestCase class that helps in creating test cases
    """
    def setUp(self):
        """
        Set up method to run before each test case.
        """
        self .new_user = User("Peter", "yang2019")

    def tearDown(self):
        """
        Tear down method that cleans up after each test case has run
        """
        User.users = []


    def test_init(self):
        """
        test_init test case to test whether the object is correctly instantiated
        """
        self.assertEqual(self.new_user.name, "Peter")
        self.assertEqual(self.new_user.login_password, "yang2019")

    def test_save_user(self):
        """
        test_save_user test case to check whether the user has successfully saved
        their account into the users list
        """
        self.new_user.save_user()
        self.assertEqual(len(User.users),1)

    def test_multiple_users(self):
        """
        test_multiple_users test case to check whether it is possible 
        for multiple users to save their accounts with password locker
        """
        self.new_user.save_user()
        test_user = User("Sharon", "sharon67")
        test_user.save_user()
        self.assertEqual(len(User.users), 2)        
