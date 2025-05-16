from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock


class MyEvent(BoxLayout):

    count = 0

    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        Clock.schedule_interval(self.callback, 5)
    
    def on_touch_up(self, touch):
        print("Touch x est egal: ", touch.x)
        print("Touch y est egal: ", touch.y)
        return super().on_touch_up(touch)
    
    def callback(self, dt):
        self.count += 1

        print("Count est : ", self.count)
        print("Temps ecouler est : ", dt)

        if self.count == 10:
            print("Last Call of my callback, by by")
            return False
        print("My callback is called")

    def callback_with_once(self, dt):
        print("Once s'executera une seule fois ", dt)


class MyApp(App):
    
    def build(self):
        return MyEvent()
    

if __name__ == "__main__":
    MyApp().run()