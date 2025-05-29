from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window


Window.set_icon("logo_256.png")


class Theme(MDScreen):
    pass

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"

        return Theme()
    
    def switch_theme_style(self):
        self.theme_cls.primary_palette = (
            "Orange" if self.theme_cls.primary_palette == "Red" else "Red"
        )
        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )


MainApp().run()