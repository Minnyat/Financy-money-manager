class login():
    def __init__(self,lang = "ru"):
        fi = lang+".xml"
        temp =fi.read()
        sefl.logintext = temp.login
