import random
import collections

Card = collections.namedtuple("Card", ["rank", "suit"])

class FrenchDeck(object):

    ranks = [str(num) for num in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        _cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
        self._cards = _cards

    def __len__(self):
        return len(self._cards)

    # __getitem__ automatically supports slicing in Python
    # __getitem__ also makes our deck iterable
    def __getitem__(self, position):
        return self._cards[position]

# sorting part
suit_values = dict(
    spades = 3, 
    hearts = 2, 
    diamonds = 1, 
    clubs = 0
    )

def spades_high(card, verbose = False):
    '''
    This function calculates a rank_value and this value is used to sort the
    FrenhDeck when usor
    '''
    rank_value = FrenchDeck.ranks.index(card.rank)
    if verbose: print(f"Rank value for card {card} is {rank_value}")
    return rank_value * len(suit_values) + suit_values[card.suit]

if __name__ == "__main__":
    french_deck = FrenchDeck()
    """ print(Card('Q', 'hearts') in french_deck)

    print(suit_values)
    print(FrenchDeck.ranks) """

    # print(french_deck._cards)

    """ for card in french_deck:
        print(card)
        print(spades_high(card)) """

    for card in sorted(french_deck, key = spades_high, reverse = True):
        print(card)

    """ print(f"Length of deck is {len(french_deck)}")
    print(f"Random item of the deck is {random.choice(french_deck)}")
    print(f"Last item of the deck {french_deck[-1]}")
    print(f"Slice of the deck {french_deck[:30]}")

    for card in french_deck:
        print(card) """