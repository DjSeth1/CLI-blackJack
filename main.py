from classes import Chips, Card, Deck, Hand

playing = True

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

    while True:
        user_input = input('Ooh, you want to hit or stand? Enter H for hit and S for stand: ')

        if user_input.lower() == 'h':
            hit(deck, hand)

        elif user_input.lower() == 's':
            print('Player stands, Dealer is playing...')
            playing = True

        else:
            print('Sorry, that please enter H or S only')
            continue
        break

def show_some(player, dealer):
    print("\n Dealer's Hand: ")
    print("", dealer.cards[1])
    
    print("\nPlayer's Hand: ", player.cards[1], sep= '\n')
    player.show_card(player, *player.cards)

def show_all(player, dealer):
    print("\n Dealers Hand:", dealer.cards.show_card(), sep= '\n')
    print("\n Dealers Value = ", dealer.value)
    print("\n PLayer's Hand ", player.cards.show_card(), sep= '\n')
    print("Player's Hand", player.value)


#game ending functions
def player_busts(player, dealer, chips):
    print("PLAYER HAS BUSTED!")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("PLAYER HAS WON!")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("DEALER HAS BUSTED!")
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print("DEALER HAS WON!")
    chips.lose_bet()

def push(player, dealer):
    print('Push! Dealer and Player have tied.')




# Gameplay

while True:
    print('===============================')
    print('Welcome to Blackjack!')

    #create and shuffle the deck
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    #PLayer's chips
    player_chips = Chips()

    #ask for bet
    take_bet(player_chips)

    #show cards
    show_some(player_hand, dealer_hand)

    
    while playing:

        hit_stand(deck, player_hand)
        
        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
        break

    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)

    print("\nPlayer's winnings stand at", player_chips.total)

    new_game = input("\nWould you like to play again? Enter 'y' or 'n': ")
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("\nThanks for playing!")
        break













        




