import random
from utils.card import card



class player:
    def __init__(self, name):
        self.name=name
        self.cards=[]
        self.turn_count=0
        self.number_of_cards=0
        self.history=[]
    # a list of Card that will contain all the cards played by the player

    def play(self):
        card_played_by_player=random.choise(self.cards)
        self.cards.remove(card_played_by_player)
       
        self.history.append(card_played_by_player)
        self.turn_count+=1
        self.number_of_cards+=1
        print(f"{card_played_by_player}")
            #card_symbol_icon\
          
          

    def __str__(self):
    
        return (f"card played by{self.name} is {card_played_by_player.value}{card_played_by_player.icon}")

class deck():
    def __init__(self):
        self.cards=[]
        self.fill_deck()

    def fill_deck(self):
        
        values=["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        suits=[Symbol("red","♥"), Symbol("red","♦"),Symbol("black","♣"),Symbol("black","♠")]
        # cards contain all the 52 cards
        for suit in suits:
            for value in values:
                self.cards.append(card(suit.color, suit.icon, value))
        # Ensure the deck has 52 cards
        #will fill cards with a complete card game'''


    def shuffle(self):
    #shuffle all the list of cards.'''
        random.shuffle(self.cards)
        print("{self.cards}")


    def distribute(self,list_of_players: list):
    #will take a list of Player as parameter and will distribute the cards evenly between all the players.'''
        no_of_players = len(list_of_players)
        cards_per_player = len(self.cards) // no_of_players
       
            
        card_index = 0
        for i, player in enumerate(list_of_players):
            player_cards = self.cards[card_index : card_index + cards_per_player]
            player.number_of_cards = len(player.cards) # Update number of cards

