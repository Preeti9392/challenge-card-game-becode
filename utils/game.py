import random
from utils.card import card
from utils.player import player

class Board:
    def __init__(self, player_names):
        self.players=[player(name) for name in player_names]           #????????????????????
        self.turn_count=0
        self.active_cards=[]
        self.history_cards=[]
        self.deck=deck()


    def start_game(self):

        self.deck.fill_deck()
        self.deck.shuffle()
        self.deck.distribute(self.players)

        for player in self.players:
            print(f"{player.name} has recieved {player.number_of_cards}")


    
        while any(player.cards for player in self.players):
            self.turn_count += 1
            self.active_cards = [] # Reset active cards for the new turn

            print(f"\n--- Turn {self.turn_count} ---")
            for player in self.players:
                if player.cards: # Only players with cards can play
                    played_card = player.play()
                    self.active_cards.append(played_card)
                else:
                    print(f"{player.name} has no cards left to play.")

            # Add active cards to history and print turn summary
            self.history_cards.extend(self.active_cards)

            print(f"Active cards : {[card for card in self.active_cards]}")
            print(f"Total cards in history: {len(self.history_cards)}")

        