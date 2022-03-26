from requestServer import callApi
class login:
    def verify(self,username = '', password = '',):
        api = callApi()
        if (api.login(username, password)):
            return True
        else: 
            return False

if __name__ == '__main__':
    tester = login() #
    print(tester.verify('admin','admin'))