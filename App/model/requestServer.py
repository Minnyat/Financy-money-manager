class callApi:
    def login( self,username = '', password = ''):
        usernameDefault = "admin"
        passwordDefault = "admin"
        if (usernameDefault == username and passwordDefault == password):
            return True 
        else: 
            return False
