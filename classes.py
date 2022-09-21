import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}



class Card:
    def __init__(self, suit, rank, values):
        self.suit = suit
        self.rank = rank
        self.value = values
        self.suit_symbol = ['♥','♦','♣','♠']
        self.values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] 


    def __str__(self):
        return self.rank + ' of ' + self.suit
    


class Deck:
    ''' Makes a Deck from Card'''
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank, values))
    
    def __str__(self):
        deck_combination = ''
        for card in self.deck:
            deck_combination += '\n' + card.__str__()
        return 'The deck has: ' +  deck_combination
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.cards = []
        self.card_values = []
        self.card_symbols = []

        self.value = 0
        self.aces = 0
         

    
    def add_card(self, card):
        self.cards.append(card)
        self.card_values.append(card.value)
        self.card_symbols.append(card.suit_symbol)

        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
    
    def ace_adjustment(self):
        while self.value > 21 and self.aces >= 1:
            self.value -= 10
            self.aces -= 1
    
    def show_card(self, suit_symbol, values):
        print( '┌───────┐')
        print(f'| {card.values:<2}    |')
        print( '|       |')
        print(f'|   {card.suit_symbol}   |')
        print( '|       |')
        print(f'|    {card.values:>2} |')
        print( '└───────┘') 
    
    def hidden_card(self):
        print('┌───────┐')
        print('|       |')
        print('|       |')
        print('|       |')
        print('|       |')
        print('|       |')
        print('└───────┘') 
    
    
class Chips:
    """Chips Class that stores and calculates bets won and lost"""

    def __init__(self):
        self.total = 100
        self.bet = 0 
    
    def win_bet(self):
        self.total += (self.bet * 2)
    
    def lose_bet(self):
        self.total -= self.bet


class Bank:
    '''Takes deposits and withdrawals for players'''

    def __init__(self):
        self.balance = 0
    
    def deposit(self):
        amount = float(input('Enter an amount to be deposited: '))
        self.balance += amount
        print(f'\n The amount deposited: {amount}')

    def withdraw(self):
        amount = float(input('Enter an amount to be withdrawn: '))
        if self.balance >= amount:
            self.balance = amount
            print(f'You withdrew: {amount}')
        else:
            print('\n Insufficient funds to withdraw')
    
    def display(self):
        print(f'\n This is your available balance: {self.balance}')
        


              

    

