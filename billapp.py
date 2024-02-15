
from kivy.uix.screenmanager import ScreenManager
from kivy.config import Config
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Config.set=("graphics", 'resizeable', True)
Window.size=(1920,1080)

class bill_soft(MDApp):
    def build(self):
        self.theme_cls.theme_style="Light"
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("kvfile/login.kv"))
        return screen_manager


if __name__ == "__main__":
    bill_soft().run()
