import collections
# This code defines a named tuple called 'Card' with two fields: 'rank' and 'suit'.
#namedtuple can be used to build classes of objects that are just bunmdles of data with no custom methods.
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
    
deck = FrenchDeck()

size = len(deck)

from random import choice
first_card = deck[0]
last_card = deck[-1]

random_card = choice(deck)

print(f"Deck size: {size}")
print(f"First card: {first_card}")
print(f"Last card: {last_card}")
print(f"Random card: {random_card}")

for card in reversed(deck):
    print(card)