from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.settings import SettingsWithSpinner
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        # Définir l'interface principale
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text='Bienvenue dans l\'application Kivy!')
        btn_settings = Button(text='Ouvrir les paramètres')
        btn_settings.bind(on_release=self.open_settings)

        layout.add_widget(self.label)
        layout.add_widget(btn_settings)
        return layout

    # Utiliser SettingsWithSpinner
    def build_settings(self, settings):
        settings.add_json_panel('Paramètres généraux', self.config, data="""
        [
            {
                "type": "title",
                "title": "Paramètres de l'application"
            },
            {
                "type": "string",
                "title": "Nom d'utilisateur",
                "desc": "Entrez votre nom",
                "section": "general",
                "key": "username"
            },
            {
                "type": "bool",
                "title": "Mode sombre",
                "desc": "Activer ou désactiver le mode sombre",
                "section": "general",
                "key": "dark_mode"
            }
        ]
        """)

    # Définir les valeurs par défaut
    def build_config(self, config):
        config.setdefaults('general', {
            'username': 'Invité',
            'dark_mode': False
        })

    # Réagir aux changements dans les paramètres
    def on_config_change(self, config, section, key, value):
        if section == 'general' and key == 'username':
            self.label.text = f"Bonjour, {value}!"
        print(f"Changement de config : [{section}] {key} = {value}")

    # Utiliser SettingsWithSpinner
    def _open_settings(self, *args):
        super().open_settings()

    def open_settings(self, *args):
        # Forcer l'utilisation de SettingsWithSpinner
        if not self._app_settings:
            self.settings_cls = SettingsWithSpinner
        self._open_settings()

if __name__ == '__main__':
    MyApp().run()
