class callApi:
    def __init__(self):
        self.serverUrl = 'http://localhost:3000/API'
        self.requests = __import__('requests')
        self.json = __import__('json')
    def login( self,username = '', password = ''):
        resq= self.requests.get(self.serverUrl+'/login?username='+username+'&password='+username)
        resJson = self.json.loads(str(resq.text))
        return resJson
if __name__ == '__main__':
    test = callApi()
    temp = test.login('admin','admin')
    print(temp)
    