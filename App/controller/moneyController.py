from App.model.database import MoneyDatabase
class Controller():
    def __init__(self) :
        
        self.model = MoneyDatabase()
      
    def getMoneyByType(self, tags: str):
        data = self.model.getHistoryAllDate()
        dates = self.model.getDate()
        res = 0
        for date in dates:
            for item in data[date]:
                if item['type'] == tags:
                    res += item['value']
        return str(res)

    def getAllMoney(self):
        data = self.model.getHistoryAllDate()
        dates = self.model.getDate()
        res = 0
        for date in dates:
            for item in data[date]:
                res += item['value']
        return str(res)


    def saveMoney(self,tags:str,money :int):
        self.model.insert(tags,money)

if __name__ == '__main__' :
    test  = Controller()
    print(test.getMoneyByType('text'))