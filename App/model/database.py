from App.Data import config
import sqlite3 as sql
from pathlib import Path

class MoneyDatabase(): 
    """Class Data interact with the database (insert, delete, update,..)"""
    def __init__(self):
        baseDir = Path(__file__).resolve().parent.parent
        self.path = baseDir /'Data'
        """The path to the directory containing the data"""
        self.database = config.database
        """Name of database"""
        self.urlDatabase = self.path / self.database
        """url of database"""
        self.sql = sql
        """sql is splite3"""
        self.key = "A"
        """Char begin of Table"""
        self.template = ['id','type','value','datetime']

    def __createTableMoney(self, tablename): 
        conn = self.sql.connect(self.urlDatabase)
        req = f"""CREATE TABLE IF NOT EXISTS {tablename} (
            id integer primary key autoincrement,
            type TEXT NOT NULL,
            value INT NOT NULL,
            datetime TEXT NOT NULL 
        );
        """
        conn.execute(req)
        conn.close()

    def __insert(self, tablename,tags, money):
        import datetime as dt

        time = dt.datetime.now().strftime("%H%M%S")
        self.__createTableMoney(tablename)
        params = (tags, money, time)
        reqInsert = f'''INSERT INTO {tablename} VALUES (NULL,?,?,?);'''
    
        conn = self.sql.connect(self.urlDatabase)
        conn.execute(reqInsert, params)
        conn.commit()
        conn.close()

    def insert(self,tags:str, money:int):
        """Insert a new money
        @arg money: The number money insert to database
        @arg tags: The type of money
        """
        import datetime as dt
        tablename = self.key + dt.datetime.now().strftime("%Y%m%d")
        self.__insert(tablename,tags,money)

    def getHistoryOnDate(self,date):
        """
        Get history of a date
        @arg date: The date to get history
        @return: List of history
        """
        tableName = self.key + date
        conn = self.sql.connect(self.urlDatabase)
        req = f"""SELECT * FROM {tableName};"""
        times = conn.execute(req)
        res = []
        for i in times:
            temp = {}
            for j in range(4):
                temp[self.template[j]] = i[j]
            res.append(temp) 
        conn.close()
        return res

    def getDate(self):
        '''
        Get dates exist in database
        @return: List of date
        '''
        conn = self.sql.connect(self.urlDatabase)
        nameDatabaseTemp = self.database.split(".")
        nameDatabase = nameDatabaseTemp[0]
        req = f"""SELECT * FROM {nameDatabase}.sqlite_master WHERE type='table';"""
        dates = conn.execute(req)
        res = []
        for i in dates:
            if i[1][0] is self.key:
                res.append(i[1][1:]) 
        conn.close()
        return res
    def getHistoryAllDate(self):
        """
        Get history of all date
        @return: dict ['<Date>']: array[dict{id, type, value, datetime}]
        """
        dates = self.getDate()
        res = {}
        for i in dates:
            res[i] = (self.getHistoryOnDate(i))
        return res

if __name__ == '__main__':
    tt = Database()


