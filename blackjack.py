from deck import DeckofCards
import time



myDeck = DeckofCards() # Instantiate my deck
print("Let's play BlackJack! You know the rules, the commands are as follows: ")
print("\t[q] Anytime to quit.")
print("\t[h] to HIT.")
print("\t[s] to Stand.")
print("\t[n] to Shuffle a new deck.")
print("\t[#] to show remainig cards in the deck.")
myDeck.shuffle() # Shuffle the new deck of cards
while True:
    play = input("Ready? ")
    if play.strip().lower() == 'n':
        myDeck.shuffle()
        # print(f'New deck ready to go, {myDeck.size} cards in the deck.')
        continue
    elif play.strip().lower() == '#':
        print(f'There are {len(myDeck.deck)} cards remaining in the deck.')    
        continue
    elif play.strip().lower() != 'q':
        myDeck.dealBlackJack() 
    while play.strip().lower() != 'q':    
        print(f'Player has {myDeck.getValueBlackJack(myDeck.player_hand)}')
        if myDeck.checkBlackJack(myDeck.player_hand):
            print('Payer Wins!')
            break
        if myDeck.getValueBlackJack(myDeck.player_hand) > 21:
            print('Player is Bust. Dealer wins! ')
            time.sleep(1)
            break
        play = input("Commands: [h] for Hit me, [s] for Stand. ")
        if play.strip().lower() == 'h':
            myDeck.hitMe(myDeck.player_hand)
            for card in myDeck.player_hand:
                time.sleep(.8)
                print(myDeck.displayCard(card))
                time.sleep(.3)
            continue
        elif play.strip().lower() == 's':
            time.sleep(1)
            print(myDeck.whoWinsBlackJack(myDeck.dealerTurn(), myDeck.getValueBlackJack(myDeck.player_hand)))
            time.sleep(1.8)
            # myDeck.dealerTurn()

            break
        else:
            continue
    print(f"Dealer's Hand: ")
    while myDeck.dealer_hand:
        time.sleep(.5)
        print(f'\t{myDeck.displayCard(myDeck.dealer_hand.pop())}')
    print(f"\nPlayer's Hand:  ")
    while myDeck.player_hand:
        time.sleep(.5)
        print(f'\t{myDeck.displayCard(myDeck.player_hand.pop())}')
    if play.strip().lower() == 'q':
        break

print(f'Remaining cards in the deck: {myDeck.size}')
