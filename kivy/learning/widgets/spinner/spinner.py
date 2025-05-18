from kivy.base import runTouchApp
from kivy.uix.spinner import Spinner
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class TestSpinner(BoxLayout):
    pass

class MyApp(App):

    def build(self):
        return TestSpinner()
    
if __name__ == "__main__":
    MyApp().run()