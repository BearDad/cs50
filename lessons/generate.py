import random

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(f"{card} ", end="")
    
print("")