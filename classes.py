import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}



class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

       

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
        return deck_combination
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        new_card = self.deck.pop()
        return new_card


class Hand:
    def __init__(self):
        self.cards = []
        self.values = 0
        self.aces = 0
         

    def add_card(self, card):
        self.cards.append(card)
        self.values += card.value
        if card.rank == 'Ace':
            self.aces += 1
    
    def ace_adjustment(self):
        while self.values > 21 and self.aces:
            self.values -= 10
            self.aces -= 1
    
    # def show_card(self, card_values, card_symbols):
    #     print( '┌───────┐')
    #     print(f'| {self.card_values:<2}    |')
    #     print( '|       |')
    #     print(f'|   {self.card_symbols}   |')
    #     print( '|       |')
    #     print(f'|    {self.card_values:>2} |')
    #     print( '└───────┘') 
    
    # def hidden_card(self):
    #     print('┌───────┐')
    #     print('|       |')
    #     print('|       |')
    #     print('|       |')
    #     print('|       |')
    #     print('|       |')
    #     print('└───────┘') 
    


        

class Player:
    '''Takes a players name and stores their balance''' 
    def __init__(self):
        self.bet = 0
        self.name = input('Please enter your name: ')
        self.balance = input('Choose a deposit amount between 1 - 1000: ')
        print(f'Hi {self.name}, you have {self.balance} as a deposit')
    
    def win_bet(self):
        self.balance += (self.bet * 2)
        print(f"Your balance is {self.balance}")
    
    def lose_bet(self):
        self.balance -= self.bet
        print(f"Your balance is {self.balance}")
    
    def push(self):
        print(f"Your balance is {self.balance}")



              

    

