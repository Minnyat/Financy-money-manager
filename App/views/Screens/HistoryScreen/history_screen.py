from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty, ObjectProperty
from App.controller.moneyController import Controller

class TopSearchBar(MDCard):
    pass

class HistoryCard(MDCard):
    """Spending Cards"""

    label_text = StringProperty()
    date_text = StringProperty()
    money_text = StringProperty()

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