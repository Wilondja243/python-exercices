from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.screenmanager import NoTransition
from kivy.lang import Builder


class SettingScreen(BoxLayout):
    pass

class MyApp(App):

    def build(self):
        
        return SettingScreen()

if __name__ == "__main__":
    MyApp().run()