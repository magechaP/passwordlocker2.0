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