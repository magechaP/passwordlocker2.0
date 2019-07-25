import unittest     #importing unittest module
from credential import Credential   # importing class Credential
import pyperclip    # importing pyperclip module

class TestCredential(unittest.TestCase):
    """
    Test class that defines the test cases for the credential class behaviours
    Args:
    unittest.TestCase: TestCase class that helps in creating test cases
    """

    def setUp(self):
        """
        Set up method to run before each test case.
        """
        self.new_credential = Credential("Sowasse","Pinterest", "sow@yi")

    def tearDown(self):
        """
        Tear down method that cleans up after each test case has run
        """  
        Credential.credentials = []
        
    def test_init(self):
        """
        test_init test case to test whether the object is correctly instantiated
        """
        self.assertEqual(self.new_credential.username, "Sowasse")
        self.assertEqual(self.new_credential.accountname, "Pinterest")
        self.assertEqual(self.new_credential.password, "sow@yi")            