from App.model.database import Money_database

class Controller():
    """Class contains functions to process data."""

    def __init__(self):
        self.model = Money_database()

    def get_money_by_type(self, tags: str):
        """
        Get the amount of the requested transaction.

        Args:
            tags (str): The transaction that you want to get the amount .

        Returns:
            The amount of the requested transaction.

        """
        
        data = self.model.get_history_all_date()
        dates = self.model.get_date()
        res = 0
        for date in dates:
            for item in data[date]:
                if item['type'] == tags:
                    res += item['value']

        res = round(res, 2)

        return str(res)

    def almost_the_same(self, tag1: str, tag2: str):
        """
        Check if two strings are almost the same.

        Args:
            tag1 (str): String you want to check.
            tag2 (str): String you want to check.

        Returns:
            bool: True if they are almost the same, False otherwise.

        """
        
        tag1 = tag1.lower()
        tag2 = tag2.lower()
        for i in range(min(len(tag1), len(tag2))):
            if(tag1[i] != tag2[i]):
                return False
        return True

    def get_all_money(self):
        """
        Calculate total amount added.

        Returns:
            The total amount.

        """
        
        data = self.model.get_history_all_date()
        dates = self.model.get_date()
        res = 0
        for date in dates:
            for item in data[date]:
                res += item['value']

        res = round(res, 2)

        return str(res)

    def convert_to_dict(self, date, data):
        """
        Save the data to a dictionary.

        Args:
            date (str): The date.
            data (dict): Dict{'type':'transaction type', 'value':'amount of money', 'datetime':'The time added spending'}.

        Returns:
            Dictionary that stores data.
        """

        Data = {}
        hour = data['datetime'][:2]
        minute = data['datetime'][2:4]
        year = date[:4]
        month = date[4:6]
        day = date[6:]

        Data['date'] = hour + ':' + minute + ' '*3 + day + '/' + month + '/' + year
        Data['type'] = data['type']
        Data['type'] = Data['type'].capitalize()
        Data['value'] = round(data['value'], 2)

        return Data

    def save_money(self, tags: str, money: float):
        """
        Save the amount you just entered into the database.


        Args:
            tags (str): The transaction that you want to add the amount.
            money (int): The amount you want to add.

        Returns:
            None
        """
        
        self.model.insert(tags, money)

    def get_latest_data(self):
        """
        Retrieve the last amount added.

        Returns:
            The last amount added.
        """
        
        import datetime as dt
        date = dt.datetime.now().strftime("%Y%m%d")
        dataOnDate = self.model.get_history_on_date(date)
        return self.convert_to_dict(date, dataOnDate[-1])

    def get_data(self):
        """
        Get all data about the amount added.

        Returns:
            All data about the amount added.
        """

        import datetime as dt
        now = dt.datetime.now()
        date_befor = now + dt.timedelta(days=-30)

        dates = []
        temp = self.model.get_date()
        if len(temp) < 1:
            max_date = (now + dt.timedelta(days=-1)).strftime("%Y%m%d")
            min_date = now.strftime("%Y%m%d")
        else:
            max_date = temp[-1]
            min_date = temp[0]

        data = self.model.get_history_all_date()
        while date_befor <= now:
            if date_befor.strftime("%Y%m%d") >= min_date and date_befor.strftime("%Y%m%d") <= max_date :
                dates.append(date_befor.strftime("%Y%m%d"))
            date_befor = date_befor + dt.timedelta(days=1)

        Data = []
        for date in dates:
            for item in data[date]:
                Data.append(self.convert_to_dict(date, item))

        return Data

    def get_total_value_of_each_transaction(self):
        """
        Get the total amount of each added transaction.

        Returns:
            Dictionary that stores the total amount of each added transaction.
        """
        
        Data = {}
        for item in self.get_data():
            if item['type'] not in Data:
                Data[item['type']] = 0
            Data[item['type']] += item['value']
            Data[item['type']] = round(Data[item['type']], 2)

        return Data

    def update_budget_value(self, value):
        """
        Update budget amount.

        Args:
            value (int): Value of money need to update.

        Returns:
            None
        """
        
        self.model.modify_user_information(budget=value)

    def get_budget_value(self):
        """
        Get budget amount.

        Returns:
            The current budget amount.
        """

        value = round(self.model.get_user_information()['budget'], 2)
        return value

    def get_remaining_budget(self):
        """
        Get remaining budget.

        Returns:
            The remaining budget amount.
        """

        return str(round(self.get_budget_value() - float(self.get_all_money()), 2))

    def get_data_base_tag(self, tag=None):
        """
        Get all added data that has the requested transaction.

        Args:
            tag (str): The transaction type.

        Returns:
            List that stores the data of the requested transaction's added amounts.
        """
        
        data = self.model.get_history_all_date()
        dates = self.model.get_date()

        Data = []

        for date in dates:
            for item in data[date]:
                cur_type = item['type']
                if(tag and self.almost_the_same(cur_type, tag) == False):
                    continue
                Data.append(self.convert_to_dict(date, item))

        return Data

if __name__ == '__main__':
    test = Controller()
    test.update_budget_value(0)