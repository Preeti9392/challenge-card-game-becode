#main file created
import random
from utils.card import card
from utils.player import player
from utils.game import game

if __name__ == "__main__":
    # Create a board with some players
    game_board = Board(player_names=["Preeti", "joy", "Char","Hina"])

    # Start the game
    game_board.start_game()
