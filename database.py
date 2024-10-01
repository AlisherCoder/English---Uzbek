import mysql.connector

class Mydb:
    def __init__(self) -> None:
        self.ConnectTB()
        self.CreateDB()
        self.CreateTB()

    def ConnectTB(self):
        self.mydb = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '953901313'
        )
        self.cursor = self.mydb.cursor()
    
    def CreateDB(self):
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS lugatbot")
        self.cursor.execute("USE lugatbot")
    
    def CreateTB(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS words(id INT AUTO_INCREMENT PRIMARY KEY,en TEXT,uz TEXT)")

    def insert(self, eng, uzb):
        self.cursor.execute("Select en from words")
        res = self.cursor.fetchall()
        lswords = [i[0] for i in res]
        
        if eng not in lswords:
            self.cursor.execute("INSERT INTO words(en,uz) values(%s,%s)", (eng, uzb))
            self.mydb.commit()
        else:
            return True
        
    def get_words(self):
        self.cursor.execute("Select en, uz from words")
        res = self.cursor.fetchall()
        return res
    
    def get_bysearch(self, key):
        self.cursor.execute(f"""Select en, uz from words where en = %s or uz = %s""",(key,key))
        res = self.cursor.fetchall()
        return res

db = Mydb()