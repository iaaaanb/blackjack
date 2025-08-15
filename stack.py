import random
from card import Card

class Stack:
    
    def __init__(self):
        self.cards = []
        self.typestring = "stack"

    def add(self, card : Card):
        if not isinstance(card, Card):
            raise ValueError("Must add a Card object")
        self.cards.append(card)
        
    def remove(self, card=None):
        
        if not self.cards:
            raise ValueError(f"Cannot remove card from empty {self.typestring}")
        
        if card is not None:
            if not isinstance(card, Card):
                raise ValueError(f"Must remove a Card object")            
            if card not in self.cards:
                raise ValueError(f"Card {card} not found in {self.typestring}")


