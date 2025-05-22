from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
# from kivy.config import Config
# from kivy.core.window import Window

# Window.borderless = False

# Config.set('graphics', 'borderless', '0')
# Config.set('graphics', 'width', '400')
# Config.set('graphics', 'height', '800')
# Config.set('grahics', 'fullscreen', '0')


class MyWidget(BoxLayout):
    pass

class MyApp(App):
    def build(self):
        return MyWidget()
    

if __name__ == "__main__":
    MyApp().run()