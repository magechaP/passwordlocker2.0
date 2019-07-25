#!/usr/bin/env python3.6
 
import random  #importing random module
from user import User #importing class User
from credential import Credential #importing class Credential

def create_credential(username,accountname,password):
    """
    create_credential function that creates an instance of the class credential
    """
    new_credential = Credential(username,accountname,password)
    return new_credential

def create_user(name, login_password):
    """
    create_user function that creates an instance of the class user
    """
    new_user = User(name,login_password)
    return new_user

def saveCredential(credential):
    """
    saveCredential function to save the credential created by the user
    """
    credential.save_credential()

def saveUser(user):
    """
    saveUser function to create a user account whenever a user
    signs up with password locker
    """
    user.save_user()

def deleteCredential(credential):
    """
    deleteCredential function that helps user delete an existing credential
    """
    credential.delete_credential()

def findCredential(account_name):
    """
    findCredential function to search for a credential by accountname and 
    return all its details
    """
    return Credential.find_accountname(account_name)

def credentialExists(account_name):
    """
    credentialExists function to check whether a credential exists
    and return True or False
    """
    return Credential.credential_exists(account_name)

def displayCredentials():
    """
    displayCredentials function to display the credentials currently saved
    """
    return Credential.display_credentials()

def displayUser():
    """
    displayUser function to display user details if user has an account
    """
    return User.display_all()

def copyUsername(account_name):
    """
    copyUsername function that enables user to copy their user name to their
    machine clip board
    """
    return Credential.copy_username(account_name)

def copyAccountname(account_name):
    """
    copyAccountname function that enables user to copy their
    accountname to the machine clipboard
    """
    return Credential.copy_accountname(account_name)

def copyPassword(account_name):
    """
    copyPassword function that enables user to copy their password 
    to the machine clipboard
    """
    return Credential.copy_password(account_name)

def main():
    user_name = input("Hello, welcome to Password_Locker. What is your name? \n")

    print("Hi {}. What would you like to do?".format(user_name))

    while True:
        userShortCodes = input("Use these shortcodes to pick an action: \n ca - Create Account \n ex - Exit Password Locker:\n")

        if userShortCodes == "ca":
            userName = input("Please enter a user name for account set up:")
            loginPassword = input("Please enter your password: ")   
            saveUser(create_user(userName, loginPassword))

            print("The following are details to your account: \n Username: {} \n password: {}".format(userName, loginPassword))
            username_login = input("Thank you for signing up with us. \n please enter your username to login: ")
            password_login = input("Please enter your password: ") 
            if loginPassword == password_login and userName == username_login:
                if User.display_all():
                    userShortCodes = input("Would you like to proceed to your credentials? Use this short code: \n  sc - See your credential: \n ")
                    if userShortCodes == "sc":

                        while True:
                            short_code = input("Use these shortcodes to choose an action: \n cc- create new credential \n delc - delete credential \n fc - find credential \n cp - copy credential \n ex - exit credentials \n dc -display credential :\n ").lower()

                            if short_code == "cc":
                                print("New Credential:")

                                username = input("Please enter your user name: \n")
                                accountname = input("Please enter your account name: \n")
                                password_choice = input("Would you like to have your password auto-generated? y/n : \n ").lower()

                                # Password generator
                                if password_choice == "n":
                                    password = input("Please enter your password: \n") 

                                else: 
                                    password_length = input("What length of password would you like to have? \n ")
                                    random_password = []
                                    for i in range (0, int(password_length)): #loop through the number of times equal to preferred length of password
                                        random_password.append(random.randint(0,9))
                                    
                                        def convert (random_password):
                                            s = [str(i) for i in random_password]
                                            res = int("".join(s))
                                            return (res)

                                    print ("Your generated password of ",password_length," characters is ", convert(random_password))
                                    password = input("Please enter the above generated password: \n")
                                response = input("Would you like to save the credential you just made? y/n: \n")
                                if response == "y":
                                    saveCredential(create_credential(username, accountname, password))
                                    print("--" * 10)
                                    print(f"credentials successfully saved! \n {username} \n {accountname} \n {password}") 
                                    print("--" * 10)

                            elif short_code == "dc":
                                if displayCredentials():
                                    print("Here is a list of all your credentials: \n")
                                    print("--" * 10)
                                    for credential in displayCredentials():
                                        print(f"{credential.username} \n {credential.accountname} \n {password}")

                                else:
                                    print("You dont seem to have any credentials saved")
                            
                            elif short_code == "fc":
                                search_accountname = input("Please enter the account you want to search for: \n")
                                if credentialExists(search_accountname):
                                    found_credential = findCredential(search_accountname)
                                    print("Account searched \n")
                                    print("-- \n" * 10)
                                    print (f"Username: {found_credential.username} \n Accountname: {found_credential.accountname} \n Password: {found_credential.password}")
                                else:
                                    print("That credential does not exist")

                            elif short_code == "cp":
                                copy_account_name = input("Please enter your accountname: ")
                                if credentialExists(copy_account_name):

                                    copy_choices = input("What would you like to copy from {}? \n pd - Password \n us - username \n ac - accountname \n".format(copy_account_name)).lower()
                                    if copy_choices == "us":
                                        copyUsername(copy_account_name)
                                        print("Username successfully copied!")
                                    elif copy_choices == "pd":
                                        copyPassword(copy_account_name)
                                        print("Password successfully copied!")

                                    elif copy_choices == "ac":
                                            copyAccountname(copy_account_name)
                                            print("Account-name successfully copied!")
                                    else: 
                                        print("{} account does not exist!".format(copy_account_name))

                            elif short_code == "delc":
                                search_accountname = input("Please enter the account you would like deleted: \n")
                                if credentialExists(search_accountname):
                                    found_credential = findCredential(search_accountname) 
                                    deleteCredential(found_credential)
                                    print(f"{search_accountname} has successfully been deleted")

                                else:
                                    print(f"{search_accountname} does not exist")

                            elif short_code == "ex":
                                print("Exiting credentials........")
                                break
                            
            else: 
                print("Incorrect username or password")

        elif userShortCodes == "ex":
            print("Logging out.......")
            break


if __name__ == '__main__':
    main()

