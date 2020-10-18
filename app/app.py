import os
import main
from time import sleep
from app.maths import maths
from app.diceroll import dice

def app():
    fin = False
    while fin != True:
        os.system('cls')
        print ("Welcome to " + main.appname)
        sleep(1)
        print ("What would you like to do? \n 1) Maths \n 2) Dice roll \n 3) Exit")

        appchoice = input(main.appname + "> ")

        if (appchoice == "1"):
            fin = True
            maths.mathintro()
        elif (appchoice == "2"):
            fin = True
            dice.roll()
        elif (appchoice == "3"):
            fin = True
            main.main()
        else:
            print ("Thats not a valid option")
            sleep(1)
            app()
