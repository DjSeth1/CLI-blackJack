from classes import Card, Deck, Hand, Player




def take_bet(player): #Ask for users bet

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
    print(f"Your total value: {player.value}")

def show_all(player, dealer):
    print("\n Dealers Hand:", dealer.cards.show_card(), sep= '\n')
    print("\n Dealers Value = ", dealer.value)
    print("\n PLayer's Hand ", player.cards.show_card(), sep= '\n')
    print("Player's Hand", player.value)


def play_again(player):
    global Playing
    if player.balance == 0:
        print('You have no more money! Thank you for playing!')
        Playing = False
    else:
        while True:
            try:
                user_input = input('Play again? (Y/N): ').upper()
            except TypeError:
                continue
            else:
                if user_input == 'N':
                    Playing = False
                    break
                elif user_input == 'Y':
                    Playing = True
                    break
                else:
                    continue




# Gameplay

print('Welcome to Blackjack!')

new_player = Player()

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


    if player_hand.value == 21 and dealer_hand.value != 21:
        show_all(dealer_hand,player_hand)
        print('BLACKJACK !!!')
        new_player.win_bet()
        play_again(new_player)
    elif player_hand.value == 21 and dealer_hand.value == 21:
        show_all(dealer_hand,player_hand)
        print('BOTH BLACKJACK !!! PUSH !!!')
        new_player.push()
        play_again(new_player)
    elif player_hand.value != 21 and dealer_hand.value == 21:
        show_all(dealer_hand,player_hand)
        print('DEALER BLACKJACK !!!')
        new_player.lose_bet()
        play_again(new_player)
    else:
        show_some(dealer_hand, player_hand)
        while player_hand.value <= 21:
            show_some(dealer_hand, player_hand)
            player_hand.ace_adjustment()
            if user_input== 'S':
                print('\nPLAYER STANDS')
                while dealer_hand.value < 18:
                    dealer_hand.add_card(new_deck.deal())
                show_all(dealer_hand, player_hand)
                if dealer_hand.value > 21:
                    print('DEALER BUST')
                    new_player.win_bet()
                    play_again(new_player)
                    break
                elif dealer_hand.value > player_hand.value:
                    print('DEALER WINS')
                    new_player.lose_bet()
                    play_again(new_player)
                    break
                elif dealer_hand.value < player_hand.value:
                    print('PLAYER WINS')
                    new_player.win_bet()
                    play_again(new_player)
                    break
                elif dealer_hand.value == player_hand.value:
                    new_player.push()
                    play_again(new_player)
                    break
        else:
            print('BUST')
            new_player.lose_bet()
            play_again(new_player)

















        




