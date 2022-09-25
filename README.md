# Welcome to BlackJack

## How the Game Works
- The game is coded to mimic a real blackjack game at a casino.
- Winning Odds and losing odds all mimic the same as a casino.
- Upon Launching the app. The user is greeted, and prompted to input their name and deposit.
- Once the user has deposited, they can choose to bet an amount less than their deposit to start the game.
- Hands for dealers and players are dealt from the Deck Class where the Card class generates each card that go into the Deck, which then go into the player or dealers hands.
- The round plays with all the relevant information being displayed using the GUI.
- The round ends at the result of many defined outcomes, and then the user is prompted to play again given they have enough balance.


## Visual Aspects of How the Game is Played

The game starts and the user is prompted to input their name:
![welcome-image](docs/Welcome-Screen.png)

Then the user is prompted to input their bets:
![take-bet-image](docs/Place-Bets.png)

After this, the round begins and cards are dealt, the GUI displays the cards, as well as their values:
![round-played-image](docs/Round-played.png)

The user can choose to hit or stand and control the flow of their game from here on out. 
![hit-or-stand-image](docs/Hit-stand-prompt.png)

After the round finishes, user can choose to play or not play again depending on their balance amount.
![play-again-image](docs/Play-again-prompt.png)

## Features

All the features outlined have a vast variety of conditionals, loops and variable scopes that work together to create a seamless and fun user experience.While this game encompasses a vast variety of features which are outlined in other deliverables of this project, the three I will outline in this document are as follows. 

### Betting Functionality  Feature

Users will be able to put their talents and luck to the test with the betting option, offering them the opportunity to improve their fortunes. They will be able to stake any amounts that fall within their deposit limits and receive the proper payout based on the odds.

### GUI display of Cards Feature

It's a card game, so the user can expect to see some cards being displayed. The programme has a graphical user interface that provides crucial information such as user balance and bets, as well as game outcomes and hand values creating a visually appealing experience.

### Hit or Stand Feature

Users can utilise the **hit** function to draw another single card to add to their hand. When the user enters the letter "h." The cards are added up to determine the player's overall hand worth. The user may also see the player's hand to determine what to do next. The hit function operates within a while loop that maintains track of the overall card hand value of the user. As long as the user's total card hand value does not exceed 21, the user is constantly prompted if they want to hit (take another card).

The stand feature works similarly to the hit, but with this case, the game ends the player’s turn and the dealers logic starts. The dealer will play till they either beat the players hand, bust or lose if they have an initial value of more than 18.



## Testing

For this project, manual testing is deployed for each of the main features.


## Help Documentation

1. If you do not have Python installed on your computer or OS, please go to [page](https://www.python.org/downloads/) and install Python.
2. Please also install pip onto your computer or OS, please go to [link](https://pip.pypa.io/en/stable/installation/)
3. Clone the repository by writing the command line below
    
    `git clone https://github.com/DjSeth1/DivijSeth_T1A3`
    
4. From here we need to change into the directory src folder from the cloned repository on our local system by: `cd DivijSeth_T1A3/` `cd src/`
5. From here we can run blackjack by executing the shell script by entering the command
    
    `./main.sh`
