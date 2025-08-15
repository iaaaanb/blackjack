class Card:

    SUITS = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, rank, suit):
        if suit not in self.SUITS:
            raise ValueError(f"Invalid suit: {suit}")
        if rank not in self.RANKS:
            raise ValueError(f"Invalid rank: {rank}")
        
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
    def __repr__(self):
        return str(self)
    
    def __eq__(self, other):
        if not isinstance(other, Card):
            return False
        return self.suit == other.suit and self.rank == self.rank
    
    def __hash__(self):
        return hash((self.suit, self.rank))