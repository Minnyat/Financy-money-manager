import sys
import os
os.environ["KIVY_NO_ARGS"] = "1"
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd_extensions.sweetalert import SweetAlert
from kivy.properties import StringProperty
from kivy.utils import get_color_from_hex
from App.views.Screens.HistoryScreen.history_screen import HistoryCard
from App.views.Screens.InputScreen.input_screen import Numpad, InputField
from App.views.Screens.RootScreen.root_screen import RootScreen
from App.controller.moneyController import Controller
from App.controller.error import Error

# Resize window
Window.size = (360, 800)

# Align the keyboard
Window.keyboard_anim_args = {'d': .2, 't': 'in_out_expo'}
Window.softinput_mode = "below_target"

def load_kv_file():
    """Load the .kv file"""
    Builder.load_file("App/views/Screens/RootScreen/root_screen.kv")

class BudgetAPP(MDApp):
    """The class used to initialize the application."""

    # Transaction type currently selected
    cur_choice = StringProperty("")

    # Amount currently selected
    cur_amount = StringProperty()

    def build(self):
        """Load the .kv file and build the application."""

        load_kv_file()
        return RootScreen()

    def __init__(self):
        """Call the `Controller` class to get and store data."""

        super(BudgetAPP, self).__init__()
        self.controller = Controller()

    def init_history(self):
        """Load the data and initialize history screen."""

        # Data import from controller
        TEXT = self.controller.get_data()

        for i in range(len(TEXT)):
            self.root.ids.History.ids.grid_banner.add_widget(
                HistoryCard(
                    label_text=TEXT[i]['type'],
                    date_text=TEXT[i]['date'],
                    money_text=str(TEXT[i]['value'])+' ₽'
                )
            )

    def init_home(self):
        """Load the data and initialize home screen."""

        Data = self.controller.get_total_value_of_each_transaction()

        for type, value in Data.items():
            exec("self.root.ids.Home.ids." + type.lower() + ".text=str(value)")
        
    def init_input(self):
        """Load the data and initialize the input screen."""

        self.input = InputField()
        self.numpad = Numpad()
        self.root.ids.Input.add_widget(self.input)
        self.root.ids.Input.add_widget(self.numpad)
        self.numpad.bind(numbers=self.numpad_pressed)

    def on_start(self):
        """Initialize home screen, input screen, history screen."""

        self.init_home()
        self.init_input()
        self.init_history()

    def show_search_data(self, tag):
        """Show searching data on history screen

        Args:
             tag (str): Search keyword

        Returns:
            A history card.
        """

        TEXT = self.controller.get_data_base_tag(tag)

        for i in range(len(TEXT)):
            self.root.ids.History.ids.grid_banner.add_widget(
                HistoryCard(
                    label_text=TEXT[i]['type'],
                    date_text=TEXT[i]['date'],
                    money_text=str(TEXT[i]['value']) + ' ₽'
                )
            )

    def numpad_pressed(self, instance, value):
        """Update the number pressed to input field.

        Args:
            value (str): value number on text field.
        """

        self.input.press_button(value)
        
        self.cur_amount = value

    def add_amount(self, amount):
        """Add the spending to total spending and transactions
        then calculate the remaining budget.
        """

        error = Error(self.cur_choice, amount)

        if error.isTrue:
            self.controller.save_money(self.cur_choice, amount)

            # Update total spending
            self.root.ids.Home.ids.cur_total.text = self.controller.get_all_money()

            # Update the remaining budget
            self.root.ids.Home.ids.remaining_budget.text =  str(self.controller.get_remaining_budget())
            
            # Update total of each transaction
            exec("self.root.ids.Home.ids." + self.cur_choice + ".text=self.controller.get_money_by_type(self.cur_choice)")
            
            # Add recent spending to History
            self.root.ids.History.add_to_history()

        # Notification about adding spending status
        SweetAlert(color_button=get_color_from_hex("#3474B9"),
                   font_style_text="H6").fire(text=error.text,
                                              type=error.type)

    def remove_widgets(self):
        """Remove all History cards."""

        self.root.ids.History.ids.grid_banner.clear_widgets()

if __name__ == "__main__":
    sys.argv[1:] = []
    BudgetAPP().run()
