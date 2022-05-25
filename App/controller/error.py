from App.model import notifications
class Error():
    def __init__(self, choice , amount):
        self.choice = choice
        self.amount = amount
        self.text = self.getText()
        self.type = self.getType()
        self.isTrue = self.check()

    def getText(self):
        error = notifications.Error(self.choice, self.amount)
        if self.choice == "":
            return error.text("no choice")
        elif self.amount == "":
            return error.text("no amount")
        elif self.amount.isdigit() == False:
            return error.text("not number")
        else:
            return error.text("success")

    def check(self):
        if self.choice == "":
            return False
        if self.amount == "":
            return False
        if self.amount.isdigit() == False:
            return False
        return True
    def getType(self):
        error = notifications.Error(self.choice, self.amount)
        if self.choice == "":
            return error.type("no choice")
        elif self.amount == "":
            return error.type("no amount")
        elif self.amount.isdigit() == False:
            return error.type("not number")
        else:
            return error.type("success")
