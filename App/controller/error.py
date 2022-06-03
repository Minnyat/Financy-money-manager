from App.model import notifications
class Error():
    def __init__(self, choice , amount):
        self.choice = choice
        self.amount = amount
        self.text = self.get_text()
        self.type = self.get_type()
        self.is_true = self.check()

    def get_text(self):
        error = notifications.Error(self.choice, self.amount)
        if self.choice == "":
            return error.text("no choice")
        elif self.amount == "":
            return error.text("no amount")
        elif self.is_number(self.amount) == False:
            return error.text("not number")
        else:
            return error.text("success")

    def check(self):
        if self.choice == "":
            return False
        if self.amount == "":
            return False
        if self.is_number(self.amount) == False:
            return False
        return True

    def get_type(self):
        error = notifications.Error(self.choice, self.amount)
        if self.choice == "":
            return error.type("no choice")
        elif self.amount == "":
            return error.type("no amount")
        elif self.is_number(self.amount) == False:
            return error.type("not number")
        else:
            return error.type("success")
    def is_number(self, x):
        try:
            a = float(x)
        except (TypeError, ValueError):
            return False
        else:
            return True
