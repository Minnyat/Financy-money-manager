class login():
    def __init__(self,lang = "ru"):
        fi = lang+".xml"
        temp =fi.read()
        self.logintext = temp.login
