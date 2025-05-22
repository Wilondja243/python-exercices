from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout


class CameraWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        Clock.shedule_interval(self.update_texture, 1.0 / 30.0)

    def update_texture(self, dt):
        camera = self.ids.cam
        preview = self.ids.preview

        if camera.texture:
            preview.texture = camera.texture

class MyApp(App):
    def build(self):
        return CameraWidget()

if __name__ == "__main__":
    MyApp().run()