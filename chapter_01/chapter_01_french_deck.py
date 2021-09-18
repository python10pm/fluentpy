import random
import collections

Card = collections.namedtuple("Card", ["rank", "suit"])

class FrenchDeck(object):

    ranks = [str(num) for num in range(2, 11)] + list("AQKJ")
    suits = "spades diamonds, clubs hearts".split()

    def __init__(self):
        _cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]
        self._cards = _cards

    def __len__(self):
        return len(self._cards)

    # __getitem__ automatically supports slicing in Python
    # __getitem__ also makes our deck iterable
    def __getitem__(self, position):
        return self._cards[position]

if __name__ == "__main__":
    french_deck = FrenchDeck()
    print(Card('Q', 'hearts') in french_deck)
    """ print(f"Length of deck is {len(french_deck)}")
    print(f"Random item of the deck is {random.choice(french_deck)}")
    print(f"Last item of the deck {french_deck[-1]}")
    print(f"Slice of the deck {french_deck[:30]}")

    for card in french_deck:
        print(card) """