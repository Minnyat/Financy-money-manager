from App.Data import config
import sqlite3 as sql
from pathlib import Path

class Money_database(): 
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
        self.user = config.userTable
        self.template = ['id','type','value','datetime']

    def __create_table_money(self, tablename): 
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

    def __create_table_user(self): 
        conn = self.sql.connect(self.urlDatabase)
        req = f"""CREATE TABLE IF NOT EXISTS {self.user} (
            id integer primary key autoincrement,
            name TEXT ,
            age TEXT,
            avatar TEXT,
            budget INT
        );
        """
        conn.execute(req)
        conn.close()

    def modify_user_information(self ,**kwargs):
        """
        Modify user information
        @arg kwargs: dict{'name':'Nhat', 'age':'21', 'avatar':'nhat.jpg', 'budget':100}
        """
        self.__create_table_user()
        conn = self.sql.connect(self.urlDatabase)
        params = {}
        params['name'] = kwargs['name'] if 'name' in kwargs else None
        params['age'] = kwargs['age'] if 'age' in kwargs else None
        params['avatar'] = kwargs['avatar'] if 'avatar' in kwargs else None
        params['budget'] = kwargs['budget'] if 'budget' in kwargs else 0
        nowData = self.get_user_information()
        if 'name' not in nowData:
            req = f"""INSERT INTO {self.user} VALUES (NULL,?,?,?,?);"""
            conn.execute(req, ('','','',params['budget']))
        else:
            for key in params:
                if params[key] is not None:
                    req = f"""UPDATE {self.user} SET {key} = {params[key]} ;"""
                    conn.execute(req)
        conn.commit()
        conn.close()

    def get_user_information(self):
        """
        Get user information
        @return: dict{'name':'Nhat', 'age':'21', 'avatar':'nhat.jpg', 'budget':100}
        """
        conn = self.sql.connect(self.urlDatabase)
        self.__create_table_user()
        req = f"""SELECT * FROM {self.user};"""
        temp = conn.execute(req)
        userInfo = temp.fetchone()
        res = {}
        res['name'] = 'cc'
        res ['name'] = userInfo[1] if userInfo is not None else None
        res['age'] = userInfo[2] if userInfo is not None else None
        res['avatar'] = userInfo[3] if userInfo is not None else None
        res['budget'] = userInfo[4] if userInfo is not None else None
        
        conn.close()
        return res


    def __insert(self, tablename,tags, money):
        import datetime as dt

        time = dt.datetime.now().strftime("%H%M%S")
        self.__create_table_money(tablename)
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

    def get_history_on_date(self,date):
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

    def get_date(self):
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
    def get_history_all_date(self):
        """
        Get history of all date
        @return: dict ['<Date>']: array[dict{id, type, value, datetime}]
        """
        dates = self.get_date()
        res = {}
        for i in dates:
            res[i] = (self.get_history_on_date(i))
        return res

if __name__ == '__main__':
    tt = Money_database()
    #tt.modify_user_information(budget = 100)
    print(tt.get_user_information())


