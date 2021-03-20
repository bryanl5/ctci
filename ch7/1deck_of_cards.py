import random

class Deck():
    def __init__(self, cards):
        self.cards = cards
    def draw(self):
        self.cards.pop()
    def shuffle(self):
        randoom.shuffle(self.cards)

class Card():
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

class Hand(Deck):
    def value(self):
        for card in self.cards:
            value += card.value
        return value