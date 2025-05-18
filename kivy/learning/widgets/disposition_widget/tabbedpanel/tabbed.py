from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.stacklayout import StackLayout


class PannelWidget(StackLayout):
    pass

class MyApp(App):
    def build(self):
        return PannelWidget()
    

MyApp().run()