import random
from random import shuffle


class Cards:
    def __init__(self):
        suits = ['H', 'D', 'C', 'S']
        values = ['A', 'K', 'Q', 'J', '2', '3',
                  '4', '5', '6', '7', '8', '9', '10']
        deck = []
        for suit in suits:
            for value in values:
                deck.append(value+suit)
        self.deck = deck

    def shuffle(self):  # shuffles the deck
        random.shuffle(self.deck)
        return self.deck

    def deal(self):  # deals a hand
        h1 = []
        h2 = []
        dealt = []
        for i in range(0, 14):
            if i % 2 == 0:
                h1.append(self.deck[i])
                del self.deck[i]
            else:
                h2.append(self.deck[i])
                del self.deck[i]
        dealt.append(h1)
        dealt.append(h2)
        return dealt

    def drawDeck(self):
        draw = random.choice(self.deck)
        self.deck.remove(draw)
        return draw
