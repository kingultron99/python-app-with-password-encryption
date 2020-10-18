import os
import main
import getpass
import sqlite3
import datetime
from app import app
from time import sleep
from passwordmanager import pwm

def newacc():
    os.system('cls')
    print ("make a new account?")
    conf = input("Y/N: ")
    conf = conf.upper()

    if (conf == "Y"):
        make()

    elif (conf == "N"):
        main.main()

    else:
        print("That's not an option")
        os.system('cls')
        newacc()

def make():
    fin = False

    while fin != True:

        os.system('cls')
        print ("Please enter your details.")


        email = input("Email: ")
        username = input("Username: ")

        conn = sqlite3.connect('./database/users.db')
        c = conn.cursor()

        c.execute("SELECT Username FROM users WHERE Username=?", (username,))
        usercheck = str(c.fetchone())

        if (usercheck is None):
            print ("there are no users in database!!")

            password = getpass.getpass("Password: ")

            if (len(password) < 5):
                print ("Please enter a password that is longer than 5 characters.")
                sleep(1)
                return
            else:

                c.execute("INSERT INTO users (Email, Username, Password, Date) VALUES (?, ?, ?, ?)", (email, username, pwm.hash_password(password), datetime.datetime.now()))
                conn.commit()

                conn.close()

                print ("Account successfully created!")
                sleep(2)
                login()

        if (username != usercheck.strip('(').strip(')').strip(',').strip('\'\'')):

            password = getpass.getpass("Password: ")

            if (len(password) < 5):
                print ("Please enter a password that is longer than 5 characters.")
                sleep(1)
                return
            else:

                c.execute("INSERT INTO users (Email, Username, Password, Date) VALUES (?, ?, ?, ?)", (email, username, pwm.hash_password(password), datetime.datetime.now()))
                conn.commit()

                conn.close()

                print ("Account successfully created!")
                sleep(2)
                login()

        elif (username == usercheck.strip('(').strip(')').strip(',').strip('\'\'')):
            print ("Username already taken")
            sleep(1)
            make()
        else:
            print ("Woah..... thats an error")
            sleep(1)
            return

def login():
    fin = False
    while fin != True:
        os.system('cls')
        print ("please enter your account details.")

        username = input("Username: ")
        password = getpass.getpass("Password: ")

        conn = sqlite3.connect('./database/users.db')
        c = conn.cursor()

        c.execute('SELECT Password FROM users WHERE Username = ?', (username,))

        stored_password = str(c.fetchone()).strip('(').strip(')').strip(',').strip('\'\'')

        conn.close()

        if (pwm.verify_password(stored_password, password) == True):
            conn.close()
            fin = True
            os.system('cls')
            print ("Welcome " + username)
            sleep(1)
            app.app()
        else:
            print ("Incorrect password.")
            print ("input password: " + password)
            print (pwm.verify_password(stored_password, password))
            print (stored_password)
            return
