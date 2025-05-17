from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout


class MyBg(GridLayout):
    pass


class MyWidget(FloatLayout):
    pass


class MyApp(App):

    def build(self):
        return MyWidget()
    

if __name__ == "__main__":
    MyApp().run()