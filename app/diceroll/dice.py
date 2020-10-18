import os
import numpy as np
from time import sleep
from app import app

def roll():
    fin = False
    while fin != True:
        os.system('cls')
        print("Rolling....")
        sleep(2)
        roll = np.random.randint(0, 6)

        print ("You rolled a " + str(roll))

        print ("Roll again?")
        choice = input("Y/N: ").lower()

        if choice == "y":
            continue
        elif choice == "n":
            fin = True
            app.app()
        else:
            fin = True
            print ("thats not a valid option!")
            sleep(1)
            app.app()
