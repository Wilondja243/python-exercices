from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import (
    ScreenManager, Screen, RiseInTransition
)


Builder.load_string('''

<MenuScreen>:
    BoxLayout:
        Button:
            text: "Go to setting"
            on_press: 
                root.manager.transition.direction = 'up'
                root.manager.current = "settings"

<SettingScreen>:
    BoxLayout:
        Button:
            text: "Back to menu"
            on_press:
                root.manager.transition.direction = 'down'
                root.manager.current = "menu"

''')


class MenuScreen(Screen):
    pass

class SettingScreen(Screen):
    pass

class TestApp(App):

    def build(self):
        sm = ScreenManager(transition=RiseInTransition())
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingScreen(name='settings'))

        return sm

if __name__ == "__main__":
    TestApp().run()