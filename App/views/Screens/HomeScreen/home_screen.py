from kivy.uix.boxlayout import BoxLayout
from kivy.utils import get_color_from_hex
from kivymd.uix.button import MDFlatButton, MDRaisedButton, MDRectangleFlatButton
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

    money_id = StringProperty()

class YourBudget(MDCard):
    """Budget balance box"""

    # Message
    msg = StringProperty()
    msg = 'Your remaining monthly budget: '

    # Balance budget
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
                    MDRaisedButton(
                        elevation=7,
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=get_color_from_hex("#424242"),
                        md_bg_color=get_color_from_hex("#FAE3D9"),
                        on_release=self.close_dialog
                    ),
                    MDRaisedButton(
                        elevation=7,
                        text="CONFIRM",
                        theme_text_color="Custom",
                        text_color=get_color_from_hex("#FFFFFF"),
                        md_bg_color=get_color_from_hex("#8AC6D1"),
                        on_release=self.neat_dialog
                    ),
                ],
            )
        self.dialog.open()

    def add_new_budget(self,value = None):
        """Get the budget number data just entered and display."""
       
        new_budget = self.dialog.content_cls.ids.new_budget.text
        self.controller.update_budget_value(int(new_budget))
        self.ids.cur_budget.text = str(self.controller.get_budget_value())+' ₽'
        self.ids.remaining_budget.text = str(self.controller.get_remaining_budget())
        
    def close_dialog(self, obj):
        """Close alert box"""

        self.dialog.dismiss()

    def neat_dialog(self, obj):
        """Confirm budget and close alert box"""

        self.add_new_budget()
        self.dialog.dismiss()
