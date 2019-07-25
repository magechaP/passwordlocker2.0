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
