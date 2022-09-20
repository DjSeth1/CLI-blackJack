from classes import Chips, Card

def take_bet(chips): #Ask for users bet

    while True:
        try:
            chips.bet = int(input('Place your bets: '))
        except ValueError:
            print('Sorry, only integers are allowed, please enter a number instead')
        else:
            if chips.bet > chips.total:
                print('You can only bet less than your total amount!')
            else:
                break

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.ace_adjustment()

def hit_stand(deck, hand):
    global playing

    while True:
        user_input = input('Ooh, you want to hit or stand? Enter H for hit and S for stand: ')

        if user_input.lower() == 'h':
            hit(deck, hand)
        elif user_input.lower() == 's':
            print('Player stands, Dealer is playing...')
            playing = False
        else:
            print('Sorry, that please enter H or S only')

def show_some(player, dealer):
    print("\n Dealer's Hand: ")
    print(hidden_card(self))
    print("", dealer.cards[1].show_card(self))
    print("\nPlayer's Hand: ", player.cards[1].show_card(self), sep= '\n')

def show_all(player, dealer):
    print("\n Dealers Hand:", dealer.cards.show_card(self), sep= '\n')
    print("\n Dealers Value = ", dealer.value)
    print("\n PLayer's Hand ", player.cards.show_card(self), sep= '\n')
    print("Player's Hand", player.value)


#game ending functions
def player_busts(player, dealer, chips):
    print("PLAYER HAS BUSTED!")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("PLAYER HAS WON!")
    chips.win_bet()

def player_wins(player, dealer, chips):
    print("PLAYER HAS WON!")
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print("DEALER HAS WON!")
    chips.lose_bet()

def push(player, dealer):
    print('Push! Dealer and Player have tied.')












        




