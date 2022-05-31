from kivy.uix.gridlayout import GridLayout
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty, ObjectProperty
from kivy.utils import get_color_from_hex
from App.views.Screens.HistoryScreen.history_screen import HistoryScreen

class InputField(MDCard):
    txt = StringProperty()
    txt = '0'
    def press_button(self, num):
        self.ids.input_txt.text = num

class AddNumpad(GridLayout):
    numbers = StringProperty()

    def __init__(self, **kwargs):
        super(AddNumpad, self).__init__(**kwargs)
        self.cols = 3
        self.padding = 40
        self.spacing = 10
        self.size_hint_y = .5
        self.row_default_height=20

        # Add button from '1' to '9'
        for i in range(1, 10):
            btn = Button(
                text=str(i),
                font_size=24,
                background_normal='',
                background_color=get_color_from_hex('#8AC6D1'),
            )
            btn.bind(on_press=self.callback)
            self.add_widget(btn)

        # Add button '.'
        btn = Button(
            text='.',
            color=get_color_from_hex("#8AC6D1"),
            background_normal='',
            font_size=50,
            background_color=get_color_from_hex('#FAFAFA'),
        )
        btn.bind(on_press=self.callback)
        self.add_widget(btn)

        # Add button '0'
        btn = Button(
            text='0',
            background_normal='',
            font_size=24,
            background_color=get_color_from_hex('#8AC6D1'),
        )
        btn.bind(on_press=self.callback)
        self.add_widget(btn)

        # Add button 'Del'
        btn = Button(
            text='Del',
            color=get_color_from_hex("#8AC6D1"),
            background_normal='',
            font_size=15,
            background_color=get_color_from_hex('#FAFAFA'),
        )
        btn.bind(on_press=self.delete_last_num)
        self.add_widget(btn)



    def callback(self, instance):
        self.numbers += instance.text
        print(self.numbers)

    def delete_last_num(self, instance):
        self.numbers = self.numbers[:-1]
        print(self.numbers)

class InputScreen(MDScreen):
    """The screen to enter the recently transacted data."""

    pass
