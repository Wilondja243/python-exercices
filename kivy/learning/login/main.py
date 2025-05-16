
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty


class LoginScreen(BoxLayout):
    
    username = ObjectProperty()
    password = ObjectProperty()
    error = ObjectProperty()

    def formValidate(self):
        if self.password.text == "" or self.username.text == "":
            self.error.text = "Les champs ne peuvent pas etre vide."
            return False
        else:
            self.error.text = f"Connexion reussue. \n Tu es le bienvenu {self.message(self.username.text)}"
            self.username.text = ""
            self.password.text = ""
            return True
    
    def message(self, name):
        return name
    

class MyApp(App):
    
    def build(self):
        return LoginScreen()
    

if __name__ == "__main__":
    MyApp().run()