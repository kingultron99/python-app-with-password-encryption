import os
from time import sleep
from app.maths.basic import mb

def addition():
    while True:
        os.system('cls')
        print ("please enter your values")

        val1 = int(input("value 1: "))
        val2 = int(input("value 2: "))

        print ("\n Any extra values? \n")

        conf = input("Y/N: ").lower()

        fin = False
        while fin != True:
            if (conf == "y"):
                print("Please enter any additional values \n if you do not require any aditional values, enter '0'")
                val3 = int(input("value 3: "))
                val4 = int(input("value 4: "))
                val5 = int(input("value 5: "))

                res = val1 / val2 / val3 / val4 / val5
                print ("result: " + str(res))

                sleep(1)
                print ("continue?")
                cont = input("Y/N").lower()
                if (cont == "y"):
                    break
                elif (cont == "n"):
                    fin = True
                    mb.basicmaths()
                else:
                    print ("Thats not a valid option!")
                    return
            elif (conf == "n"):
                res = val1 / val2
                print ("result: " + str(res))

                sleep(1)
                print ("continue?")
                cont = input("Y/N").lower()
                if (cont == "y"):
                    break
                elif (cont == "n"):
                    fin = True
                    mb.basicmaths()
                else:
                    print ("Thats not a valid option!")
                    return
            else:
                print ("Thats not a valid option!")
                return
        return
