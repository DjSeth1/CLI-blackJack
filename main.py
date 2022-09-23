from classes import Deck, Hand, Player

import time
import clearing



def take_bet(player): #Ask for users bet
    '''Asks user for a bet amount
        Args: player

        Returns:
        An input corresponding to the bet amount    
    '''
    while True:
        try:
            player.bet = int(input('Place your bets: '))
        except ValueError:
            print('Sorry, only integers are allowed, please enter a number instead')
        else:
            if  player.bet > player.balance:
                print('You can only bet less than your total amount!')
            else:
                break

def hit(deck, hand):
    ''' takes a card from a deck and gives it to the player hand or dealer hand upon asking for a hit using the add card function from class hand and ace-adjustment to calculate ace value based on hand value

    args: deck and hand

    returns
    a card from the deck to player or dealer

    '''
    hand.add_card(deck.deal())
    hand.ace_adjustment()

def hit_stand(deck, hand):
    ''' allows user to input whether or not they want to hit or stand proceeding into the next round
    
    args: deck and hand

    returns: if hit, adds a new card to the players hand using add_card function
    if stand, dealers turn comes on and it adds cards to the dealer until dealer stands
    '''

    while True:
        user_input = input('Ooh, you want to hit or stand? Enter H or hit and S for stand: ')
        print(user_input)

        try:
            if user_input.lower() == 'h':
                print("HIT")
                time.sleep(1)
                hit(deck, hand)
                hand.show_card(hand.cards[-1])    
            elif user_input.lower() == 's':
                print("STAND")
                time.sleep(1)
                print('Player stands, Dealer is playing...')
                return 's' 
        except ValueError:
            print('Sorry, that cannot be taken please enter H or S only')
        else:
            break
       

        

def show_some(dealer_hand, player_hand):
    ''' active until player stands, shows the cards in player and dealers hands
    
    args: dealer_hand and player_hand

    returns: 
    cards in dealer and player hands with ASCII art aswell as text display of cards
    '''
    print("\n Dealer's Hand: ")
    print("", dealer_hand.cards[1])
    if len(dealer_hand.cards)<10:

        dealer_hand.show_card(dealer_hand.cards[1])
        dealer_hand.hidden_card()

    else:
        for card in dealer_hand.cards:
            dealer_hand.show_card(card)
    
    print("\nPlayer's Hand: ")
    for card in player_hand.cards:
        print("", card)
        print(player_hand.show_card(card))
    print(f"Your total value: {player_hand.values}")

def show_all(dealer_hand, player_hand):
    ''' active when player has stood, and displays all cards in hand of players and dealers
    
    args: dealer_hand and player_hand

    returns: cards in dealer and players hands aswell as text of each card and the total value of the hand.

    '''
    print("\n Dealers Hand:", sep= '\n')
    for card in dealer_hand.cards:
        time.sleep(0.5)
        dealer_hand.show_card(card)
    print("\n Dealers Value = ", dealer_hand.values)
    print("\n PLayer's Hand ", sep= '\n')
    for card in player_hand.cards:
        time.sleep(0.5)
        player_hand.show_card(card)
    print("Player's Hand", player_hand.values)


def play_again(player):
    '''Prompts user to play again depending on whether or not they have enough cash deposited to play
    
    args: player

    returns:
    if player does not have enough cash it exits the game
    if player has enough cash:
    if player wants to play, it starts a new game with and prompts a bet amount

    else player does not want to play it exits and allows users to cash out their winnings.

    '''
    global Playing
    if player.balance == 0:
        print('You have no more money! Thank you for playing!')
        Playing = False
    else:
        while True:
            try:
                user_input = input('Play again? (Y/N): ').upper()
            except TypeError:
                print('Please enter a string of either Y or N only')
            except ValueError:
                print('PLease enter Y or N only')
                continue
            else:
                if user_input == 'N':
                    Playing = False
                    print("This is your cashout amount", player.balance)
                    print('Thanks for playing!')
                    break
                elif user_input == 'Y':
                    Playing = True
                    break
                else:
                    continue




# Gameplay

clearing.clear()

print('Welcome to Blackjack!')

new_player = Player()
deck = Deck()
hand = Hand()
Playing = True



while Playing:
    take_bet(new_player)
    new_deck = Deck()
    new_deck.shuffle()
    player_hand = Hand()
    dealer_hand = Hand()
    player_hand.add_card(new_deck.deal())
    dealer_hand.add_card(new_deck.deal())
    player_hand.add_card(new_deck.deal())
    dealer_hand.add_card(new_deck.deal())


    if player_hand.values == 21 and dealer_hand.values != 21:
        show_all(dealer_hand,player_hand)
        print('BLACKJACK !!!')
        new_player.win_bet()
        play_again(new_player)


    elif player_hand.values == 21 and dealer_hand.values == 21:
        show_all(dealer_hand,player_hand)
        print('BOTH BLACKJACK !!! PUSH !!!')
        new_player.push()
        play_again(new_player)


    elif player_hand.values != 21 and dealer_hand.values == 21:
        show_all(dealer_hand,player_hand)
        print('DEALER BLACKJACK !!!')
        new_player.lose_bet()
        play_again(new_player)


    else:
        show_some(dealer_hand, player_hand)


        while player_hand.values <= 21:
            show_some(dealer_hand, player_hand)
            player_hand.ace_adjustment()


            if hit_stand(deck, player_hand) == 's':
                print('\nPLAYER STANDS')
                while dealer_hand.values < 18:
                    dealer_hand.add_card(new_deck.deal())
                show_all(dealer_hand, player_hand)


                if dealer_hand.values > 21:
                    print('DEALER BUST')
                    new_player.win_bet()
                    play_again(new_player)
                    clearing.clear()
                    break


                elif dealer_hand.values > player_hand.values:
                    print('DEALER WINS')
                    new_player.lose_bet()
                    play_again(new_player)
                    clearing.clear()
                    break


                elif dealer_hand.values < player_hand.values:
                    print('PLAYER WINS')
                    new_player.win_bet()
                    play_again(new_player)
                    
                    break


                elif dealer_hand.values == player_hand.values:
                    print('IT IS A PUSH!')
                    new_player.push()
                    play_again(new_player)
                    clearing.clear()
                    break
        else:
            print('BUST')
            new_player.lose_bet()
            play_again(new_player)
            clearing.clear()

















        




