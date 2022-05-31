from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd_extensions.sweetalert import SweetAlert
from kivy.properties import StringProperty
from kivy.utils import get_color_from_hex
from App.views.Screens.HistoryScreen.history_screen import HistoryCard, TopSearchBar
from App.views.Screens.HomeScreen.home_screen import HomeCard, YourBudget
from App.views.Screens.InputScreen.input_screen import AddNumpad, InputField
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

    cur_choice = StringProperty("")

    # Số tiền đang nhập vào
    cur_amount = StringProperty()

    def __init__(self):
        super(BudgetAPP, self).__init__()
        self.controller = Controller()

    def build(self):
        """Load the .kv file and build the application."""

        load_kv_file()
        return RootScreen()

    def init_history(self):
        """Load the data of the history."""

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
        """Load the data of the home screen."""

        # *** Nối label_id, label_text, money_text với database ***
        for i in range(8):
            self.root.ids.Home.ids.home_layout.add_widget(
                HomeCard(
                    label_id='id', # ID của transaction
                    label_text='type', # type(tên) của transaction
                    money_text='money' # Tổng tiền của mỗi transaction
                )
            )

        # *** nối "balc" với data là số dư còn lại ***
        self.root.ids.Home.add_widget(
            YourBudget(
                balc='???',
                md_bg_color=get_color_from_hex("#FAE3D9")
            )
        )

    def init_input(self):
        """Load the data of the input screen."""

        self.input = InputField()
        self.numpad = AddNumpad()
        self.root.ids.Input.add_widget(self.input)
        self.root.ids.Input.add_widget(self.numpad)
        self.numpad.bind(numbers=self.numpad_pressed)

    def on_start(self):
        """Show the data from history and home screen everytime run the application"""

        self.init_history()
        self.init_home()
        self.init_input()


    def numpad_pressed(self, instance, value):
        """Update the number pressed to input field."""

        self.input.press_button(value)

        # Cập nhật biến số tiền vừa nhập vào
        self.cur_amount = value

    def add_amount(self, amount):
        """add the spending to total spending and transactions"""

        error = Error(self.cur_choice, amount)

        if error.isTrue:
            self.controller.save_money(self.cur_choice, amount)

            # *** Sửa lại đường dẫn data cho các thẻ transaction trong HomeScreen ***
            # *** Cập nhật lại số dư ***

            # Update total spending
            self.root.ids.Home.ids.cur_total.text = self.controller.get_all_money()

            # Update total of each transaction
            exec("self.root.ids.Home.ids." + self.cur_choice + ".text=self.controller.get_money_by_type(self.cur_choice)")

            # Add recent spending to History
            self.root.ids.History.add_to_history()

        # Notification about adding spending status
        SweetAlert(color_button=get_color_from_hex("#3474B9"),
                   font_style_text="H6").fire(text=error.text,
                                              type=error.type)

if __name__ == "__main__":
    BudgetAPP().run()
