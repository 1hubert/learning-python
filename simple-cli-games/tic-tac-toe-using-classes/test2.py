import random
import numpy


class Player:
    def __init__(self, letter):
        self.letter = letter  # X or O

    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        """Get a random valid spot for computer's next move."""
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        """Get a random valid spot for our next move."""
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            # we're going o check that this is a correct value by trying to cast
            # it to an integer, and if it's not, then we say it's invalid
            # if that spot is not available on the board, we also say its invalid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError

                valid_square = True  # if these are succesful, then yay!
            except ValueError:
                print('Invalid square. Try again.')

        return val

prayer = Player('X')
two_b = HumanPlayer('X')
amalgamate = RandomComputerPlayer('X')

test_subject = HumanPlayer(prayer)


import math
print()
print(type(math))