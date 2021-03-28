import enum
import random

class Suit(enum.Enum):
    heart = 1
    diamond = 2
    club = 3
    spade = 4
    joker_red = 5
    joker_black = 6

class Card():
    def __init__(self, value = None, suit = None , is_joker = False):
        if is_joker:
            self.value = 14 #1-13 is reserved for normal cards
            self.suit = suit
        else:
            self.value = value #int
            self.suit = suit #enum
        self.is_joker = is_joker
        if not self.is_valid_card():
            raise Exception("not a valid carrd")

    def is_valid_card(self): return True#{...}

class Deck():
    def __init__(self, cards = None):
        self.cards = cards #list of cards
        if not cards:
            #create standard deck of cards
    def draw(self):
        self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)

class BlackjackDeck(Deck):
    def __init__(self):
        self.cards = #loop through suits and numbers 1-13 to create blackjack deck of cards

class BlackjackGame():
    def __init__(self, hand1, hand2):
        self.hand1 = hand1 #BlackjackHank
        self.hand2 = hand2 #BlackjackHank
        self.deck = BlackjackDeck()
        self.current_turn = 1

    def play_turn(self):
        if self.current_turn == 1:
            print(self.hand1.get_score())
            #ask hand1 if they want to hit or stay
            while hit:
                self.hand1.add_card()
                if self.hand1.get_score() > 21:
                    print("player 1 busted")
                    return
                #ask hand1 if they want to hit or stay
            self.current_turn = 2
            self.hand1.did_stay = True
        else:
            print(self.hand2.get_score())
            #ask hand2 if they want to hit or stay
            while hit:
                self.hand2.add_card()
                if self.hand2.get_score() > 21:
                    print("player 2 busted")
                    return
                #ask hand2 if they want to hit or stay
            self.current_turn = 1
            self.hand2.did_stay = True

        if self.hand1.did_stay and self.hand2.did_stay:
            self.end_game()

    def end_game(self):
        if self.hand1.get_score() > self.hand2.get_score():
            print("player 1 won")
        else:
            print("player 2 won")

class Hand():
    def __init__(self, cards = None):
        if not cards:
            self.cards = []
        else:
            self.cards = cards #list of cards

    def add_card(self, card):
        self.cards.append(card)

class BlackjackHand(Hand):
    def __init__(self, cards):
        #error check for if there are only 2 cards
        self.cards = cards
        self.did_stay = False

    def get_score(self):
        score = 0
        num_aces = 0
        for card in self.cards:
            if card.value == 1:
                score += 11
                num_aces += 1
            elif card.value <= 10:
                score += card.value
            else:
                score += 10
        while score > 21 or num_aces == 0:
            score -= 10
            num_aces -= 1
        return score

    def is_busted(self):
        if self.get_score > 21:
            return True
        return False
    

# import random

# class Deck():
#     def __init__(self, cards):
#         self.cards = cards
#     def draw(self):
#         self.cards.pop()
#     def shuffle(self):
#         random.shuffle(self.cards)

# class Card():
#     def __init__(self, value, suit):
#         self.value = value
#         self.suit = suit

# class Hand(Deck):
#     def value(self):
#         for card in self.cards:
#             value += card.value
#         return value