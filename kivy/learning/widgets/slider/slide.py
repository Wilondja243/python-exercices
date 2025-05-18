from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty


class MySlide(BoxLayout):
    pass

class MySliderApp(App):
    def build(self):
        return MySlide()
    

if __name__ == "__main__":
    MySliderApp().run()