from kivy.utils import get_color_from_hex
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty, ObjectProperty
from App.controller.moneyController import Controller

class TopSearchBar(MDCard):
    """Searching bar"""

    def __init__(self, **kwargs):
        super(TopSearchBar, self).__init__(**kwargs)
        self.elevation = 5
        self.ripple_behavior = True
        self.size_hint = (None, None)
        self.size = ("360dp", "60dp")
        self.md_bg_color = get_color_from_hex("#f4dedc")

class HistoryCard(MDCard):
    """Spending Cards"""

    label_text = StringProperty()
    date_text = StringProperty()
    money_text = StringProperty()

    def __init__(self, **kwargs):
        super(HistoryCard, self).__init__(**kwargs)
        self.padding = 10
        self.height = 200
        self.radius = 7
        self.elevation = 1

class HistoryScreen(Screen):
    """The screen displays the data of the transactions."""

    def __init__(self, **kwargs):
        super(HistoryScreen, self).__init__(**kwargs)
        self.controller = Controller()

    def add_to_history(self):
        """Add recent transaction data to history."""

        # Data import from controller
        data = self.controller.get_latest_data()

        self.ids.grid_banner.add_widget(
            HistoryCard(
                label_text=data['type'],
                date_text=data['date'],
                money_text=str(data['value']) + ' ₽'
            )
        )