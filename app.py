from SQL_connector import Football, General, History
from utilts import Data
from color import *

def app():

    print(f" {GREEN}*************************   WELECOME TO PLAYING QUIZE GAME   ******************************** {REST}")
    while True:

        permission = input(f"Do you want play a quize game? ")

        if permission == "yes":
            input(f"{BLUE}please press enter to play game{REST}")
            print(f" {RED}  Catagories-A\t\t\t\t\tCatagories-B\t\t\t\tCatagories-C\n{LBLUE}\tFootBall\t\t\t\t\tGeneral\t\t\t\t\t\t\tHistory{REST}")

            select = input(f"{LGREEN}pelase select you favorite catagories:{REST} ")
            if select == "FootBall":
                Object = Football()
                Object.run_ball()
                Object=Data()
                Object.DB()


            elif select == "General":
                object = General()
                object.run_genral()
                Object = Data()
                Object.DB()

            elif select == "History":
                object = History()
                object.run_history()
                Object = Data()
                Object.DB()

        else:
            print("byeeeee")
            exit(0)