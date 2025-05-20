from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class VideoWidget(BoxLayout):
    pass

class MyApp(App):
    def build(self):
        return VideoWidget()
    

MyApp().run()