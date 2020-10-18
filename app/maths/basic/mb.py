import os
import numpy as np
from app.maths import maths
from app.maths.basic.add import add
from app.maths.basic.sub import sub
from app.maths.basic.div import div
from app.maths.basic.mult import mult

def basicmaths():
    while True:
        os.system('cls')
        print ("Select an option: \n 1) Addition \n 2) Subtraction \n 3) Multiplication \n 4) Division \n 5) Back")
        choice = input("> ")

        if (choice == "1"):
            add.addition()
        elif (choice == "2"):
            sub.subtraction()
        elif (choice == "3"):
            mult.multiplication()
        elif (choice == "4"):
            div.division()
        elif (choice == "5"):
            maths.mathintro()
