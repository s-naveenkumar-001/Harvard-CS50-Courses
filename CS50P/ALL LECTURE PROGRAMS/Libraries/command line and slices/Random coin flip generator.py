# In this program we import the random library to flip the coin heads or tails.
# from the random library we import the choice module.
# In python documention " random.choice(seq) ". sequence means list we create a list of items to flip the coin.
# This random coin flip program we give two item so its give equal of fifty percentage of probability. the random choice probaility will change based on the no of items. 

from random import choice
coin = choice(["Heads", "Tails"])
print(coin)