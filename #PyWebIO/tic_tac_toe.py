import time
import random

from pywebio import start_server
from pywebio.output import use_scope, put_html, toast, put_table, put_buttons
from pywebio.session import set_env

board_size = 3
board = [
    # -1 -> none, 0 -> O, 1 -> X 
    #board[row][column] = 0/1
    [-1] * board_size
    for _ in range(board_size)
]


def check_rows():
    if board[0][0] != -1 and board[0][0] == board[0][1] == board[0][2]:
        return True
    elif board[1][0] != -1 and board[1][0] == board[1][1] == board[1][2]:
        return True
    elif board[2][0] != -1 and board[2][0] == board[2][1] == board[2][2]:
        return True


def check_columns():
    if board[0][0] != -1 and board[0][0] == board[1][0] == board[2][0]:
        return True
    elif board[0][1] != -1 and board[0][1] == board[1][1] == board[2][1]:
        return True
    elif board[0][2] != -1 and board[0][2] == board[1][2] == board[2][2]:
        return True


def check_diagonals():
    if board[0][0] != -1 and board[0][0] == board[1][1] == board[2][2]:
        return True
    elif board[0][2] != -1 and board[0][2] == board[1][1] == board[2][0]:
        return True


def check_win():
    if check_rows():
        return True
    elif check_columns():
        return True
    elif check_diagonals():
        return True
    else:
        return False


def check_tie():
    for row in board:
        for elem in row:
            if elem == -1:
                return False
    return True


current_symbol = 0


def main():
    game_on = True

    # Prevent animated reloadings of the board.
    set_env(output_animation=False)
    
    # Custom formatting.
    put_html("""<style> table th, table td { padding: 0px !important;} button {padding: .75rem!important; margin:0!important} </style>""")  # Custom styles to make the board more beautiful

    def reset(z):
        global board
        global game_on
        board = [[-1] * board_size for _ in range(board_size)]
        show_board()
        game_on = True
        main()

    def change_player():
        global current_symbol
        if check_tie() == False and check_win() == False:        
            if current_symbol == 0:
                current_symbol = 1
                print('player changed to 1')
            elif current_symbol == 1:
                current_symbol = 0
                print('player changed to 0')

    def set_stone(pos):
        if game_on:
            x, y = pos
            board[x][y] = current_symbol
            change_player()
            show_board()

    # Remove the previous board before showing current board.
    @use_scope('board', clear=True)
    def show_board():
        table = [
            [
                put_buttons([dict(label=' ', value=(x, y), color='light')], onclick=set_stone) if cell == -1 else [' ⭕', ' ❌'][cell]
                for y, cell in enumerate(row)
            ]
            for x, row in enumerate(board)
        ]
        put_table(table)
        put_buttons(['Reset'], onclick=reset)

    show_board()

    while game_on:
        
        while current_symbol == 1:
            x = random.randint(0, 2)
            y = random.randint(0, 2)
            if board[x][y] == -1:
                board[x][y] = current_symbol
                change_player()
                show_board()
                break
                
        if check_win():
            toast(f"{current_symbol} wins!", color='green')
            game_on = False
        elif check_tie():
            toast("it's a tie!", color='error')
            game_on = False

        time.sleep(0.2)

        
        


start_server(main, port=80, debug=True)
