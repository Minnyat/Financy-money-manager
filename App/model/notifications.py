from App.Data.error import error

class Error():
    def __init__(self, choice , amount):
        self.data = error
    def text(self,smg:str):
        if smg in self.data:
            return self.data[smg]
        else: return("no smg in data")