import math
import random

class Player:
    def __init__(self, letter):
        self.letter = letter
    
    # we want all players to get their next moves given a game
    def get_move(self, game):
        pass
    
class RandomComputerPlayer(Player):
    def __int__(self, letter):
        super().__init__(letter)
        
    def get_move(self ,game):
        pass
    
class HumanPlayer(Player):
    def __int__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        
        valid_sqaure = False
        val = None
        while not valid_sqaure:
            square = input("self.letter +'\'s turn. Input move(0-9)")
            #we're going to check that this is a correct value by trying to cast
            #it to an integer , and if it's not, then we say its invalid
            #if that spot is not available on the board, we also say its invalid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
            except ValueError:
                print("Invalid sqaure. Try again.")
        return val
    