def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c

    return None, None


def is_valid(puzzle, guess, row, col):
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    
    sq = (row//3, col//3)
    for x in range(sq[0]*3, sq[0]*3+3):
        for y in range(sq[1]*3, sq[1]*3+3):
            if guess == puzzle[x][y]:
                return False
    
    return True

def sudoku_solver(puzzle):
    row, column = find_next_empty(puzzle)
    
    if row is None:
        return True
    
    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, column):
            puzzle[row][column] = guess
            # now recurse using this puzzle
            # recursively call our function
            if sudoku_solver(puzzle):
                return True
        
        # if not valid OR if our guess does not solve the puzzle
        # we need to backtrack and try a new number
        puzzle[row][column] = -1  # reset the guess

    # If none of the numbers that we try work, then this puzzle is unsolvable
    return False

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]

    print(sudoku_solver(example_board))
    [print(row) for row in example_board]
            
