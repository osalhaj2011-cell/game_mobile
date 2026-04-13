from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle

class Game(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(0.2, 0.6, 1)
            self.player = Rectangle(pos=(200, 300), size=(50, 50))

class MyApp(App):
    def build(self):
        return Game()

if __name__ == "__main__":
    MyApp().run()
