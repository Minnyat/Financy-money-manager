from App.Data.notifications import error,type

class Error():
    def __init__(self, choice , amount):
        self.data = error
        self.typeList = type

    def text(self,smg:str):
        if smg in self.data:
            return self.data[smg]
        else:
            self.data['None']

    def type(self,smg:str):
        if smg in self.typeList:
            return self.typeList[smg]
        else:
            self.typeList['None']

