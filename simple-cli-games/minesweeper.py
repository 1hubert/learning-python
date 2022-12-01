from multiprocessing.sharedctypes import Value
import random
import re

class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size  # dimension size
        self.num_bombs = num_bombs
        
        self.board = self.make_new_board()  # plant the BOMBO PAU PAU
        self.assign_values_to_board()

        # initialize a set to keep track of which locations we've uncovered
        # we'll save (row, col) tuples into this set
        self.dug = set()

    def make_new_board(self):
        """Construct a new board based on the dim size and num bombs.
        We should construct the list of the lists here (or whatever structure you prefer,
        but since we have a 2-D board, list of lists is most natural)"""
        
        # generate a new board
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        # plant the BOMBA
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2-1)
            row = loc // self.dim_size
            col = loc % self.dim_size

            if board[row][col] == '*':
                continue

            board[row][col] = '*'
            bombs_planted += 1
        
        return board

    def assign_values_to_board(self):
        """Now that we have the bombs planted , let's assign a num 0-8 for all the empty
        spaces that represents how many neighbouring bombs there are. we can precompute these
        and  it'll save us some effort checking what's around the board later on."""
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    # if  this is already a bomb, we don't want to calculate anything
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)

    def get_num_neighboring_bombs(self, row, col):
        # let's iterate through each of the neighbouring positions and sum
        # number of bombs. make sure not to go out of bounds!
        num_neighboring_bombs = 0
        for r in range(max(0, row-1), min(self.dim_size-1, (row+1)) + 1):
            for c in range(max(0, col-1), min(self.dim_size-1, (col+1)) + 1):
                if r == row and c == col:
                    # our original location, don't check
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1

        return num_neighboring_bombs
        
    def dig(self, row, col):
        # dig at that location, return True if successful, False if bomb dug

        self.dug.add((row, col))

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True

        # self.board[row][col] must be 0 then
        for r in range(max(0, row-1), min(self.dim_size-1, (row+1) + 1)):
            for c in range(max(0, col-1), min(self.dim_size-1, (col+1)+1)):
                if (r, c) in self.dug:
                    continue # already dug
                self.dig(r, c)
        
        # if our initial dig didn't hit a bomb we shouldn't hit a bomb here
        return True

    def __str__(self):
        # When you call print on this object it's gonna show the board to the player

        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '

        # put this together in a string
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep


def play(dim_size=4, num_bombs=2):
    # Step 1: create the board and plant the bombs
    board = Board(dim_size, num_bombs)

    # Step 2: show the user the board and ask for where they want to DIG
    
        
    # Step 3a: if location is a bomb, show game over message
    # Step 3b: if location is not a bomb, digrecursively until each square is at least
    #          next to a bomb 
    # Step 4: repeat steps 2 and 3a/b until there are no more places to dig -> VICTORY!
    safe = True
    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        # 0,0 or 0, 0 or 0,  0
        valid_input = False
        while not valid_input:
            try:
                user_input = (input('WHERE would you like to dig? Input as row,col: ')).split(',')
                if len(user_input) != 2: raise ValueError
                row, col = int(user_input[0].strip()), int(user_input[1].strip())

                if row < 0 or row >= board.dim_size or col < 0 or col >= board.dim_size:
                    print('You can\'t dig there. Try again!')
                    continue

                valid_input = True
            except ValueError:
                print('This is not a valid input. Try again!')
            except IndexError:
                print('Seperate row and column values with a comma. Try again!')
        
        # if it's valid, we dig
        safe = board.dig(row, col)
        if not safe:
            # dug a bomb ahhhhhhhh
            break # game over................

    # 2 ways to end loop, lets check which one
    if safe:
        print('CONGRATULATIONS!! YOU ARE VICTORIOUS!!!')
    else:
        print('GAME OVER :(')
        # let's reveal everything
        board.dug = [(r, c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)

if __name__ == '__main__':
    play()
    