import pyodbc

class Data:
    def __init__(self):
        self.conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL "
                                   "Server};SERVER=LAPTOP-58MDPDG0;"
                                   "DATABASE=QUIZE;"
                                   "Trusted_connection=yes")
        self.corsor = self.conn.cursor()


    def DB(self):

        num = int(input("your id: "))
        namef = input("enyetr your first name:  ")
        namel = input("enter your last name:  ")
        scores = int(input("enter your score:  "))
        catagory = input("enter the  catagories you plyed:  ")
        self.corsor.execute("INSERT INTO Table_score(Id,fname,lname,score,catagories) values(?,?,?,?,?)", (num, namef, namel, scores,catagory))
        self.conn.commit()
