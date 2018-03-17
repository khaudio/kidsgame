#!/usr/bin/env python
"""
Kids' game where a letter is displayed onscreen, and the player must type
the displayed key to advance
"""

from getch import getch
from random import choice


class LetterGame:
    def __init__(self):
        self.alphabet = [
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
            ]
        self.used = []

    def attempt(self, letter):
        while True:
            entry = getch().lower()
            if ord(entry) is 27:
                return False
            elif entry == letter:
                print('Yay!')
                return True

    def challenge(self):
        if sorted(self.used) == sorted(self.alphabet):
            self.used = []
        letter = choice(list(set(self.alphabet).difference(set(self.used))))
        self.used.append(letter)
        print(letter.upper())
        return letter

    def play(self):
        while True:
            letter = self.challenge()
            yield letter
            if not self.attempt(letter):
                break


if __name__ == '__main__':
    LetterGame().play()
