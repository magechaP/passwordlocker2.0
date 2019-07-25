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
    User.save_user()

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