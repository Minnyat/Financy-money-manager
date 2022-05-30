from kivy.uix.boxlayout import BoxLayout
from kivy.utils import get_color_from_hex
from kivymd.uix.button import MDFlatButton
from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from App.controller.moneyController import Controller

class Content(BoxLayout):
    """Dialog box"""
    pass

class HomeCard(MDCard):
    """The cards represent the amount of each type of spending."""

    #Name of the transaction type
    label_text = StringProperty()

    #Total money of each transaction type
    money_text = StringProperty()

    #Transaction id
    label_id = StringProperty()

class YourBudget(MDCard):
    """Budget balance box"""

    #message
    msg = StringProperty()
    msg = 'Your remaining monthly budget: '

    #Balance budget
    balc = StringProperty()

class HomeScreen(Screen):
    """Home screen, showing total spending, budget balance."""

    dialog = None

    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        self.controller = Controller()

    def show_alert_dialog(self):
        """The dialog box appears each time a new budget number for the month is entered."""

        if not self.dialog:
            self.dialog = MDDialog(
                title="[font=App/views/assets/Fonts/Inter/static/Inter-Light.ttf]"
                      "Enter your projected spending for this month."
                      "[/font]",
                type="custom",
                content_cls=Content(),
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=get_color_from_hex("#3474B9"),
                        on_release=self.close_dialog
                    ),
                    MDFlatButton(
                        text="CONFIRM",
                        theme_text_color="Custom",
                        text_color=get_color_from_hex("#3474B9"),
                        on_release=self.neat_dialog
                    ),
                ],
            )
        self.dialog.open()

    def add_new_budget(self):
        """Get the budget number data just entered and display."""

        # ***Thêm một hàm lưu lại số dư của tháng, nối data***

        # New budget for this month
        new_budget = self.dialog.content_cls.ids.new_budget.text
        self.ids.cur_budget.text = new_budget+' ₽'

    def close_dialog(self, obj):
        """Close alert box"""

        self.dialog.dismiss()

    def neat_dialog(self, obj):
        """Confirm budget and close alert box"""

        self.add_new_budget()
        self.dialog.dismiss()
