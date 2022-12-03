from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder


kv = Builder.load_string("""
Screen:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Setting Screen'
        Button:
            text: 'Exit'
            on_release: app.stop()
""")


class SettingScreen(App):

    def build(self):
        return kv



Window.top = 50
Window.left = 50
Window.size = (300, 300)
if __name__ == "__main__":
    SettingScreen().run()