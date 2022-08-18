from logging import NullHandler
from random import randint
import time


class DeckofCards():
    def __init__(self, deck = [], player_hand = [], dealer_hand = [], size = 52):
        self.size = size
        self.deck = deck
        self.player_hand = player_hand
        self.dealer_hand = dealer_hand
    
    def shuffle(self): # Doesn't actually shuffle, just creates/populates a new deck of cards
        if self.size >= 0:
            self.deck.clear()
            print(f'I just cleared the deck, and this is whats in it: {self.deck}')
        i, j = 0, 1
        suit = 'Hearts'
        while i <= 51: # Generate new deck, list of dictionaries of i:j, where i is an int 0-51 (index), and j is an int 1-13 (for each suit)
            while j <= 13:
                if i < 13:
                    suit = 'Hearts'
                elif i < 26:
                    suit = 'Spades'
                elif i < 39:
                    suit = 'Diamonds'
                else:
                    suit = 'Clubs'

                self.deck.append({'suit': suit, 'value': (j if j < 10 else 10), 'pip': '', 'BlkJk': False})
                if j == 1:
                    self.deck[i]['pip'] = 'Ace'
                    self.deck[i]['BlkJk'] = True
                    self.deck[i]['value'] = 11
                elif j < 11:
                    self.deck[i]['pip'] = str(j)
                elif j == 11:
                    self.deck[i]['pip'] = 'Jack'
                    self.deck[i]['BlkJk'] = True
                elif j == 12:
                    self.deck[i]['pip'] = 'Queen'
                elif j == 13:
                    self.deck[i]['pip'] = 'King'
                i += 1
                j += 1
            j = 1
        if self.size == 52:
            print(f'New deck is ready to deal, {len(self.deck)} cards remaining.')
        else:
            time.sleep(.3)
            print(f'{len(self.deck)} cards remaining.')
        return self.deck

    def throwTheCards(self):
        print(self.deck)
    
    def dealACard(self):
        if self.size > 0:
            card = self.deck.pop((randint(1, self.size))-1)
            self.size -= 1
            return card
        else:
            return f'The deck is empty! Time to shuffle.'
        
    def player(self):
        pass

    def displayCard(self, card): # Returns an f string with the card data formatted in readable english
        return f"{card['pip']} of {card['suit']}"

    def dealBlackJack(self):
        self.dealer_hand = []
        self.player_hand = []
        self.dealer_hand.append(self.dealACard())
        self.dealer_hand.append(self.dealACard())
        time.sleep(1)
        print(f"Dealer's Card: {self.displayCard(self.dealer_hand[1])} \n")
        if self.checkBlackJack(self.dealer_hand) == True:
            print(f'Dealer has BlackJack: {self.displayCard(self.dealer_hand[0])} {self.displayCard(self.dealer_hand[1])}')
        self.player_hand.append(self.dealACard())
        time.sleep(1)
        self.player_hand.append(self.dealACard())
        time.sleep(1)
        print(f"Player's Hand: {self.displayCard(self.player_hand[0])}, {self.displayCard(self.player_hand[1])} ")
        if self.checkBlackJack(self.player_hand) == True:
            print(f'Player has BlackJack: {self.displayCard(self.player_hand[0])} {self.displayCard(self.player_hand[1])}')
            self.whoWinsBlackJack(self.getValueBlackJack(self.dealer_hand), self.getValueBlackJack(self.player_hand))
    
    def checkBlackJack(self, hand):
        if (hand[0]['BlkJk']== True) and (hand[1]['BlkJk'] == True) and (self.getValueBlackJack(hand) == 21):
            return True
        else: 
            return False
    
    def getValueBlackJack(self, hand):
        value = 0
        ace = False
        for card in hand:
            value += card['value']
            if card['pip'] == 'Ace':
                ace = True
        if value > 21 and ace == True:
            value -= 10
        return value

    def dealerTurn(self):
        not_bust = True
        while not_bust:
            dealer_score = self.getValueBlackJack(self.dealer_hand)
            if dealer_score < 16:
                self.hitMe(self.dealer_hand)
                time.sleep(.5)
                print(f'Dealer hits: \n\t {self.displayCard(self.dealer_hand[-1])}')
                continue
            elif dealer_score > 21:
                not_bust = False
                continue
            elif dealer_score > 16:
                break
        return dealer_score

    def whoWinsBlackJack(self, dealer_score, player_score):
        time.sleep(1)
        print(f'Dealer Score is {dealer_score}.')
        time.sleep(1)
        if dealer_score > 21:
            time.sleep(.5)
            return f'Dealer has {dealer_score}; Dealer busts. Player wins!'
        elif dealer_score > player_score:
            time.sleep(.5)
            return f'Dealer has {dealer_score}. \nPlayer has {player_score}. Dealer wins!'
        elif dealer_score < player_score:
            time.sleep(.5)
            return f'Dealer has {dealer_score}. \nPlayer has {player_score}. Player wins!'
        elif dealer_score == player_score:
            time.sleep(.5)
            return f'Dealer and Player are tied. Push!'
        else:
            return f'I am super confused.'
    
    def hitMe(self, hand):
        return hand.append(self.dealACard())

