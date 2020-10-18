import os
from app import app
from app.maths.basic import mb
from app.maths.trig import mt

def mathintro():
    fin = False
    while fin != True:
        os.system('cls')
        print ("Select an option: \n 1) basic maths \n 2) trigonometry \n 3) Back")
        mintchoice = input("> ")

        if (mintchoice == "1"):
            fin = True
            mb.basicmaths()
        elif (mintchoice == "2"):
            fin = True
            mt.trigonometry()
        elif (mintchoice == "3"):
            fin = True
            app.app()
        else:
            print("Thats not a valid option")
            return
