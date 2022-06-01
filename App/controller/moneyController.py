from App.model.database import Money_database
class Controller():

    def __init__(self):
        self.model = Money_database()
      
    def get_money_by_type(self, tags: str):
        data = self.model.get_history_all_date()
        dates = self.model.get_date()
        res = 0
        for date in dates:
            for item in data[date]:
                if item['type'] == tags:
                    res += item['value']

        return str(res)

    def get_all_money(self):
        data = self.model.get_history_all_date()
        dates = self.model.get_date()
        res = 0
        for date in dates:
            for item in data[date]:
                res += item['value']

        return str(res)

    def convert_to_dict(self, date, data):

        Data = {}
        year = date[:4]
        month = date[4:6]
        day = date[6:]

        Data['date'] = day + '/' + month + '/' + year
        Data['type'] = data['type']
        Data['type'] = Data['type'].capitalize()
        Data['value'] = data['value']

        return Data

    def save_money(self, tags:str, money:int):
        self.model.insert(tags, money)

    def get_latest_data(self):

        import datetime as dt
        date = dt.datetime.now().strftime("%Y%m%d")
        dataOnDate = self.model.get_history_on_date(date)
        return self.convert_to_dict(date, dataOnDate[-1])

    def get_data(self):

        data = self.model.get_history_all_date()
        dates = self.model.get_date()
        Data = []
        for date in dates :
            for item in data[date]:
                Data.append(self.convert_to_dict(date, item))

        return Data

    def get_total_value_of_each_transaction(self):
        Data = {}
        for item in self.get_data():
            if item['type'] not in Data :
                Data[item['type']] = 0
            Data[item['type']] += item['value']
        return Data
        
    def update_budget_value(self,value) :
        self.model.modify_user_information(budget = value)
        print(self.model.get_user_information()['budget'])
       
    
    def get_budget_value(self) :
        return self.model.get_user_information()['budget']

        
    def get_remaining_budget(self) :
        return str(self.get_budget_value() - int(self.get_all_money()))
     
    def get_data_base_tag(self,tag=None):
        
        data = self.model.get_history_all_date()
        dates = self.model.get_date()
        
        Data = []
        for date in dates :
            for item in data[date]:
                cur_type = item['type'] 
                if(tag and cur_type[0] != tag[0] ) :
                    continue 
                Data.append(self.convert_to_dict(date, item))
        return Data

if __name__ == '__main__':
    test = Controller()
    test.update_budget_value(budget=1000)
    