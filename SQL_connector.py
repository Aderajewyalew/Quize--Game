
from  color import  *
from utilts import *

class Football(Data):

    def __init__(self):
        super().__init__()

    def run_ball(self):
        self.corsor.execute("SELECT Question,option1,option2,option3,option4,Answer FROM Table_Quize where id between 1 and 6")
        score = 0
        for row in self.corsor:
            print(row[0], "\n", row[1], "\n", row[2], "\n", row[3], "\n", row[4])
            user = input("enter your answer:")
            if user == row[5]:
                score+=1
                print(f"{GREEN}    Correct!!  your score is {REST}----{score}/{6} ")

            else:
                print(f"{RED}Incorrect ")
                print(f"The coorect answer is {row[5]} {GREEN} your score is {REST} ------{score}/{6}")
        print(f"{YELLOW}Your total score is  ------{score}/{6}")
        print("Your score in percent is ------", score / 6 * 100, "%",REST,)


class General(Football):

    def run_genral(self):
        self.corsor.execute("SELECT Question,option1,option2,option3,option4,Answer FROM Table_Quize where id between 7 and 11")
        score = 0
        for row in self.corsor:
            print(row[0], "\n", row[1], "\n", row[2], "\n", row[3], "\n", row[4])
            user = input("enter your answer:")
            if user == row[5]:
                score+=1
                print(f"{GREEN}    Correct!!  your score is {REST}----{score}/{5} ")
            else:
                print(f"{RED}Incorrect ")
                print(f"The coorect answer is {row[5]}  {GREEN}your score is {REST} ------{score}/{5}")
        print(f"{YELLOW}Your total score is  ------{score}/{5}")
        print("Your score in percent is ------", score / 5 * 100, "%",REST,)


class History(Football):

    def run_history(self):
        self.corsor.execute(
            "SELECT Question,option1,option2,option3,option4,Answer FROM Table_Quize where id between 12 and 17")
        score = 0
        for row in self.corsor:
            print(row[0], "\n", row[1], "\n", row[2], "\n", row[3], "\n", row[4])
            user = input("enter your answer:")
            if user == row[5]:
                score+=1
                print(f"{GREEN}    Correct!!  your score is {REST}----{score}/{6} ")
            else:
                print(f"{RED}Incorrect ")
                print(f"The coorect answer is {row[5]} {GREEN}your score is {REST} ------{score}/{6}")
        print(f"{YELLOW}Your total score is  ------{score}/{6}")
        print("Your score in percent is ------", score / 6 * 100, "%",REST,)