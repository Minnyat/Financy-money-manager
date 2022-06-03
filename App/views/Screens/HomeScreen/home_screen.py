from kivy.uix.boxlayout import BoxLayout
from kivy.utils import get_color_from_hex
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivymd_extensions.sweetalert import SweetAlert
from App.controller.error import Error

from App.controller.moneyController import Controller

class Content(BoxLayout):
    """Content in the dialog box."""
    pass

class HomeCard(MDCard):
    """The cards represent the amount of each type of spending."""

    #Name of the transaction type
    label_text = StringProperty()

    #Total money of each transaction type
    money_text = StringProperty()

    #Transaction id
    money_id = StringProperty()

class YourBudget(MDCard):
    """Budget balance box"""

    # Text message
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
        """The dialog box appears each time a new budget
         number for the month is entered."""

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

    def add_new_budget(self, value=None):
        """Get the budget number data just entered and display."""

        new_budget = self.dialog.content_cls.ids.new_budget.text
        error = Error('budget', new_budget)

        if error.is_true:
            self.controller.update_budget_value(float(new_budget))
            self.ids.cur_budget.text = str(self.controller.get_budget_value()) + ' ₽'
            self.ids.remaining_budget.text = str(self.controller.get_remaining_budget())

        SweetAlert(color_button=get_color_from_hex("#3474B9"),
                   font_style_text="H6").fire(text=error.text,
                                              type=error.type)

    def close_dialog(self, obj):
        """Close alert box without doing anything."""

        self.dialog.dismiss()

    def neat_dialog(self, obj):
        """Confirm budget and close alert box."""

        self.add_new_budget()
        self.dialog.dismiss()
