import importlib
import os

from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd_extensions.sweetalert import SweetAlert
from kivy.properties import StringProperty
from kivy.utils import get_color_from_hex
from App.views.Screens.RootScreen.root_screen import RootScreen
from App.controller.moneyController import Controller
from App.controller.error import Error


Window.size = (360, 800)

def load_kv_file():
    Builder.load_file("App/views/Screens/RootScreen/root_screen.kv")

class BudgetAPP(MDApp):
    cur_choice = StringProperty("")
    

    def __init__(self):
        super(BudgetAPP, self).__init__()
        self.controller = Controller()

    def build(self):
        load_kv_file()
        return RootScreen()

    def add_amount(self, amount):
        error = Error(self.cur_choice, amount)
        if error.isTrue:
            self.controller.saveMoney(self.cur_choice, amount)
            self.root.ids.Home.ids.cur_total.text = self.controller.getAllMoney()
            exec("self.root.ids.Home.ids." + self.cur_choice + ".text=self.controller.getMoneyByType(self.cur_choice)")
        SweetAlert(color_button=get_color_from_hex("#3474B9"),font_style_text="H6").fire(text=error.text)

    
        
        
        
            


if __name__ == "__main__":
    BudgetAPP().run()
