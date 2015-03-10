from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

class StudomaticWidget(Widget):
    pass

class StudomaticApp(App):
    def build(self):
        parent = Widget()
        Client = StudomaticWidget()
        Tap = Label(text='Tap Your Card')
        parent.add_widget(Tap)
        parent.add_widget(Client)
        Window.clearcolor = (0, 0, 0, 1)
        return parent

if __name__ == '__main__':
    StudomaticApp().run()