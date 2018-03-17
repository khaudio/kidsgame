#!/usr/bin/env python

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from letter_loop import *

class KidsGame(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        game = LetterGame()
        self.ids.current.text = ''

    def play(self):
        for letter in game.loop():
            self.ids.current.text = letter


class KidsGameApp(App):
    pass

if __name__ == '__main__':
    KidsGameApp().run()
