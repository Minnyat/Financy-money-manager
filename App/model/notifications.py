from App.Data.notifications import error, type

class Error():
    """notification to show on screen."""
    def __init__(self, choice, amount):
        self.data = error
        """error to show on sreen"""
        self.typeList = type
        """type of error"""

    def text(self, msg: str):
        if msg in self.data:
            return self.data[msg]
        else:
            self.data['None']

    def type(self, msg: str):
        if msg in self.typeList:
            return self.typeList[msg]
        else:
            self.typeList['None']

