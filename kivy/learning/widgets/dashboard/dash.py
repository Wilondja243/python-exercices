from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout


class Dashboard(BoxLayout):
    pass


class MyApp(App):
    def build(self):
        return Dashboard()
    

if __name__ == "__main__":
    MyApp().run()