import kivy.clock
import kivymd.uix.textfield
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
Window.size = (360, 800)

class Login(Screen):

    def __init__(self, **kwargs):
        super(Login, self).__init__(**kwargs)
        self.cur = 0
        self.main_label = ["WELCOME TO FINANCY", "ДОБРО ПОЖАЛОВАТЬ В ФИНАНСЫ"]
        self.user_hint_text = ["Username", "Имя пользователя"]
        self.pass_hint_text = ["Password", "Пароль"]
        self.login_button = ["Login", "Авторизоваться"]

    def Switch_Language(self):
        global cur
        #temp = self.ids.MainLabel.text
        if self.cur == 0:
            self.cur = 1
            self.ids.lang_button.icon = "assets/en_language.png"
        else:
            self.cur = 0
            self.ids.lang_button.icon = "assets/ru_language.png"

        self.ids.MainLabel.text = self.main_label[self.cur]
        self.ids.Username.hint_text = self.user_hint_text[self.cur]
        self.ids.Password.hint_text = self.pass_hint_text[self.cur]
        self.ids.Login_Button.text = self.login_button[self.cur]



class Register(Screen):
    pass

class View(MDApp):

    def __init__(self):
        super().__init__()
        self.main_label = ["WELCOME TO FINANCY", "ДОБРО ПОЖАЛОВАТЬ В ФИНАНСЫ"]
        self.user_hint_text = ["Username", "Имя пользователя"]
        self.pass_hint_text = ["Password", "Пароль"]
        self.login_button = ["Login", "Авторизоваться"]

    #self.controller.ChangeLanguage("RU",main_label,user_hint_text, pass_hint_text, login_button)

    def build(self): #build and load .kv file
        global screen_manager
        screen_manager = ScreenManager(transition=kivy.uix.screenmanager.WipeTransition())

        kv = Builder.load_file("login.kv")
        screen_manager.add_widget(Login(name="login"))

        screen_manager.add_widget(Register(name="register"))
        #kv = Builder.load_file("login_ru.kv")
        #screen_manager.add_widget(log_ru(name="login_ru"))

        return screen_manager


    def get_data(self, Username, Password): #get data from input username and password
        print("Username: ", Username)
        print("Password: ", Password)
        print('\n')

    def getname(self):
        usn = (self.root.get_screen("menu").ids.userdata.text)
        self.root.ids.label.text = usn



if __name__ == "__main__":
    View().run()
