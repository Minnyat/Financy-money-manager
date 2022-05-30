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
from App.views.Screens.RootScreen.root_screen import RootScreen
from App.controller.moneyController import Controller
from App.controller.error import Error

Window.size = (360, 800)

def load_kv_file():
    """Load the .kv file"""
    Builder.load_file("App/views/Screens/RootScreen/root_screen.kv")

class BudgetAPP(MDApp):
    """The class used to initialize the application."""

    cur_choice = StringProperty("")

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


        self.root.ids.History.add_widget(
            TopSearchBar()
        )

    def init_home(self):
        """Load the data of the home screen."""

        for i in range(8):
            self.root.ids.Home.ids.home_layout.add_widget(
                HomeCard(
                    label_id='id',
                    label_text='type',
                    money_text='money'
                )
            )

        self.root.ids.Home.add_widget(
            YourBudget(
                md_bg_color=get_color_from_hex("#ABCED9")
            )
        )

    def on_start(self):
        """Show the data from history and home screen everytime run the application"""
        self.init_history()
        self.init_home()

    def add_amount(self, amount):
        """add the spending to total spending and transactions"""

        error = Error(self.cur_choice, amount)

        if error.isTrue:
            self.controller.save_money(self.cur_choice, amount)

            # Sửa lại đường dẫn data cho các thẻ transaction trong HomeScreen
            self.root.ids.Home.ids.cur_total.text = self.controller.get_all_money()
            exec("self.root.ids.Home.ids." + self.cur_choice + ".text=self.controller.get_money_by_type(self.cur_choice)")
            self.root.ids.History.add_to_history()
        SweetAlert(color_button=get_color_from_hex("#3474B9"),
                   font_style_text="H6").fire(text=error.text,
                                              type=error.type)

if __name__ == "__main__":
    BudgetAPP().run()
