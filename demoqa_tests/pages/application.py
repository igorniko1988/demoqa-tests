from .registration import Registration
from .text_box import TextBox
from .left_panel import LeftPanel


class Application:
    def __init__(self):
        self.registration = Registration()
        self.text_box = TextBox()
        self.left_panel = LeftPanel()


app = Application()