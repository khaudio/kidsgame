#!/usr/bin/env python

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from threading import Thread
from letter_loop import *


class KidsGame(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.loop = Thread(target=self.play)
        self.loop.start()

    def play(self):
        game = LetterGame()
        while True:
            letter = game.challenge()
            self.ids.challenge.text = letter.upper()
            if not game.attempt(letter):
                break


class KidsGameApp(App):
    pass


if __name__ == '__main__':
    KidsGameApp().run()
