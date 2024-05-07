# In this program we shuffle three cards.
# from random we import the shuffle module.
# In python documentation random.shuffle(x).
# first import the library and next create a list of itmes to shuffle and use the shuffle module.
# we use for loop to print the items one after another.usin print we print the shuffled cards.

from random import shuffle
cards = ["jack", "king", "queen"]
shuffle(cards)
for card in cards:
    print(card)
