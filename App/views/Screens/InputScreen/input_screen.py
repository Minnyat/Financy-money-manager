from kivy.uix.gridlayout import GridLayout
from kivymd.uix.card import MDCard
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, ObjectProperty
from kivy.utils import get_color_from_hex

class InputField(MDCard):
    """Text field showing the entered number.
    The default value of the text field is `0`
    """

    txt = StringProperty()
    txt = '0'

    def __init__(self, **kwargs):
        super(InputField, self).__init__(**kwargs)
        self.md_bg_color = get_color_from_hex("#8AC6D1")
        self.pos_hint = {'center_y': .5}
        self.size_hint_y = None
        self.size = (360,60)

    def press_button(self, num):
        """Update number pressed to text field."""

        self.ids.input_txt.text = num

class Numpad(GridLayout):
    """Create a numpad"""

    # The current sequence of numbers being entered.
    numbers = StringProperty()

    def __init__(self, **kwargs):
        super(Numpad, self).__init__(**kwargs)
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
        """Add the last number entered to the sequence."""

        self.numbers += instance.text

    def delete_last_num(self, instance):
        """Delete the last entered number."""

        self.numbers = self.numbers[:-1]

class SaveButton(Button):
    """A button to save the entered spending."""

    def __init__(self, **kwargs):
        super(SaveButton, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (60, 30)
        self.text = 'save'
        self.halign = 'center'
        self.color = get_color_from_hex("#212121")
        self.font_size = 15
        self.font_name = "App/views/assets/Fonts/Inter/static/Inter-Bold.ttf"
        self.pos_hint = {"center_x": .85, "center_y": .952}
        self.background_normal = ''
        self.background_color = get_color_from_hex('#BBDED6')

class InputScreen(Screen):
    """The screen to enter the recently transacted data."""

    pass
