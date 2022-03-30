from requestServer import callApi
class login:
    def verify(self,username = '', password = '',):
        api = callApi()
        return api.login(username, password)

if __name__ == '__main__':
    tester = login() #
    print(tester.verify('admin','admin'))