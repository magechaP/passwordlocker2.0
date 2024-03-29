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
        self.new_credential = Credential("Peter","Instagram", "2019")

    def tearDown(self):
        """
        Tear down method that cleans up after each test case has run
        """  
        Credential.credentials = []
        
    def test_init(self):
        """
        test_init test case to test whether the object is correctly instantiated
        """
        self.assertEqual(self.new_credential.username, "Peter")
        self.assertEqual(self.new_credential.accountname, "Instagram")
        self.assertEqual(self.new_credential.password, "2019")            

    def test_save_credential(self):
        """
        test_save_credential test case to check whether credential is successfully saved
        """
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credentials), 1)

    def test_save_multiple_credentials(self):
        """
        test_save_multiple_credentials test case to check whether a user can save multiple credentials
        """
        self.new_credential.save_credential()
        test_credential = Credential ("Peter", "Instagram","2019")
        test_credential.save_credential()
        self.assertEqual(len(Credential.credentials), 2)

    def test_delete_credential(self):
        """
        test_delete_credential test case to test if user can delete an
        already saved credential
        """
        self.new_credential.save_credential()
        test_credential = Credential("Peter", "Instagram","2019")
        test_credential.save_credential()
        test_credential.delete_credential()
        self.assertEqual(len(Credential.credentials),1)

    def test_find_credential_by_accountname(self):
        """
        test_find_credential_by_accountname testcase to test if user is able to search for an a saved credential 
        by its accountname
        """
        self.new_credential.save_credential()
        test_credential = Credential("Peter", "Instagram", "2019")
        test_credential.save_credential()
        found_credential = Credential.find_accountname("Instagram")
        self.assertEqual(found_credential.accountname, test_credential.accountname)


    def test_credential_exists(self):
        """
        test_credential_exists test case to check whether a credential exists within credentials saved
        """
        self.new_credential.save_credential()
        test_credential = Credential("Peter", "Instagram", "2019")
        test_credential.save_credential()

        credential_exists = Credential.credential_exists("Instagram")
        self.assertTrue(credential_exists)

    def test_display_all_credentials(self):
        """
        test_display_all_credentials test case to test whether a user is able to view all the credentials they have saved within 
        password locker
        """
        self.new_credential.save_credential()
        test_credential = Credential("Peter", "Instagram", "2019")
        test_credential.save_credential()
        self.assertEqual(Credential.display_credentials(), Credential.credentials)

    def test_copy_username(self):
        """
        test_copy_username to test if user can copy their username to their machine clipboard
        """
        self.new_credential.save_credential()
        Credential.copy_accountname("Instagram")
        self.assertEqual(self.new_credential.username, pyperclip.paste())

    def test_copy_accountname(self):
        """
        test_copy_accountname to test if user can copy their accountname to their machine clipboard
        """

        self.new_credential.save_credential()
        Credential.copy_accountname("Instagram")
        self.assertEqual(self.new_credential.accountname,pyperclip.paste())

    def test_copy_password(self):
        """
        test_copy_password to test if user can copy their password to their machine clipboard
        """

        self.new_credential.save_credential()
        Credential.copy_password("Pinterest")
        self.assertEqual(self.new_credential.password,pyperclip.paste())


if __name__ == '__main__':
    unittest.main()                                        