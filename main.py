from replit import db as database
from cryptography.fernet import Fernet
import os
import json

def generate_and_store_key():
    key = Fernet.generate_key()
    with open("encryption_key.txt", "wb") as f:
        f.write(key)
    return key

def load_key():
    return open("encryption_key.txt", "rb").read()

if not os.path.exists("encryption_key.txt"):  
    key = generate_and_store_key()
else:
    key = load_key()

f = Fernet(key)

while True:
    choice = input("Do you want to (1) Sign Up or (2) Log In? ")

    if choice == "1":

        username = input("Create your username: ")
        password = input("Create your password: ")


        encrypted_username = f.encrypt(username.encode()).decode()
        encrypted_password = f.encrypt(password.encode()).decode()
 
        database.set(username, {"username": encrypted_username, "password": encrypted_password})



        print("Sign up successful!")

    elif choice == "2":                  
        username = input("Enter your username: ")
        password = input("Enter your password: ")


        user_data = database.get(username)

        if user_data:
                                   
            stored_encrypted_username = user_data["username"].encode()
            stored_encrypted_password = user_data["password"].encode()

            stored_username = f.decrypt(stored_encrypted_username).decode()
            stored_password = f.decrypt(stored_encrypted_password).decode()

                                    
            if username == stored_username and password == stored_password:
                print("Logged in!")
                break
            else:
                print("Login failed - Incorrect username or password.")
        else:
            print("Username not found.")

    else:
        print("Invalid choice, please enter 1 or 2")