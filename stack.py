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
        
    def remove(self, card=None, count=1):
        """Remove specific card or n cards from top of stack"""
        if not self.cards:
            raise ValueError(f"Cannot remove card from empty {self.typestring}")
        
        if card is not None:
            # Remove specific card
            if not isinstance(card, Card):
                raise ValueError(f"Must remove a Card object")            
            if card not in self.cards:
                raise ValueError(f"Card {card} not found in {self.typestring}")
            
            self.cards.remove(card)
            return card
        else:
            # Remove n cards from top
            if count < 1:
                raise ValueError("Count must be at least 1")
            if count > len(self.cards):
                raise ValueError(f"Cannot remove {count} cards, only {len(self.cards)} available")
            
            if count == 1:
                return self.cards.pop()
            else:
                # Remove multiple cards from the end
                removed_cards = []
                for _ in range(count):
                    removed_cards.append(self.cards.pop())
                return removed_cards
    
    def remove_all(self):
        """Remove and return all cards from the stack"""
        all_cards = self.cards[:]
        self.cards.clear()
        return all_cards
    
    # Sorting

    def shuffle(self):
        random.shuffle(self.cards)

    def sort_by_suit(self):
        """Sort cards in hand by suit, then by rank."""
        suit_order = {suit: i for i, suit in enumerate(Card.SUITS)}
        rank_order = {rank: i for i, rank in enumerate(Card.RANKS)}

        self.cards.sort(key=lambda card: (suit_order[card.suit], rank_order[card.rank]))

    def sort_by_rank(self):
        """Sort cards in hand by rank, then by suit."""
        suit_order = {suit: i for i, suit in enumerate(Card.SUITS)}
        rank_order = {rank: i for i, rank in enumerate(Card.RANKS)}
        
        self.cards.sort(key=lambda card: (rank_order[card.rank], suit_order[card.suit]))
    
    def get_cards_by_suit(self, suit): 
        """Return all cards of a specific suit."""
        if suit in Card.SUITS:
            return [card for card in self.cards if card.suit == suit]
        
        raise ValueError(f"'{suit}' is not a valid suit. "
                    f"Valid suits: {Card.SUITS}")
    
    def get_cards_by_rank(self, rank):
        """Return all cards of a specific rank."""
        if rank in Card.RANKS:
            return [card for card in self.cards if card.rank == rank]   
        raise ValueError(f"'{rank}' is not a valid rank. "
                        f"Valid ranks: {Card.RANKS}")


    # Counting
    def count(self, attribute):
        # Check if it's a valid suit
        if attribute in Card.SUITS:
            return sum(1 for card in self.cards if card.suit == attribute)
        
        # Check if it's a valid rank
        elif attribute in Card.RANKS:
            return sum(1 for card in self.cards if card.rank == attribute)
        
        # Invalid attribute
        else:
            raise ValueError(f"'{attribute}' is not a valid suit or rank. "
                            f"Valid suits: {Card.SUITS}. Valid ranks: {Card.RANKS}")


    # Info

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.cards) == 0
    
    def __len__(self):
        """Return the number of cards using len() function."""
        return len(self.cards)

    def __iter__(self):
        """Make deck iterable."""
        return iter(self.cards)

    def __getitem__(self, index):
        return self.cards[index]