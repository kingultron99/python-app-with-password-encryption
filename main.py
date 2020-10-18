import os
import acc
from app import app
from time import sleep

appname = "App"

def main():
    # Clears the screen

    os.system('cls')

    os.system('title ' + appname)
    #greeting text

    print ("Welcome! \n 1) Login \n 2) New Account \n 3) Exit")
    greet = input("> ")

    if (greet == "1"):
        acc.login()

    elif (greet == "2"):
        acc.newacc()

    elif (greet == "3"):
        os.system('cls')
        os.system('exit')

    else:
        print("that's not a valid function!")
        sleep(2)
        os.system('cls')
        main()






if __name__ == "__main__":
    main()
