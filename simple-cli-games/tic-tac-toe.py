import random

player_A = 'player'
player_B = 'bot'
current_player = player_A
game_on = True
print()
print("The game has started!")
print("Make your move by typing number from 1 to 9")
print(player_A + "\'s symbol is \"O\"")
print(player_B + "\'s symbol is \"X\"")
print()


board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


def check_rows():
    if board[0] != "-" and board[0] == board[1] == board[2]:
        return True
    elif board[3] != "-" and board[3] == board[4] == board[5]:
        return True
    elif board[6] != "-" and board[6] == board[7] == board[8]:
        return True

def check_columns():
    if board[0] != "-" and board[0] == board[3] == board[6]:
        return True
    elif board[1] != "-" and board[1] == board[4] == board[7]:
        return True
    elif board[2] != "-" and board[2] == board[5] == board[8]:
        return True

def check_diagonals():
    if board[0] != "-" and board[0] == board[4] == board[8]:
        return True
    elif board[2] != "-" and board[2] == board[4] == board[6]:
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
    for elem in board:
        if elem == "-":
            return False
    return True


def flip_player():
    global current_player
    if current_player == player_A:
        current_player = player_B
    else:
        current_player = player_A

symbol = "O"

def play():
    global game_on
    global symbol
    print("It is " + current_player + "\'s turn now.")
    if symbol == "O":
        symbol = "X"
    else:
        symbol = "O"

    if current_player == "bot":
        choice = str(random.randint(1,9))
        while choice == False or board[int(choice[0]) - 1] != "-":
            choice = str(random.randint(1,9))
    else:
        display_board()
        choice = input("Your move: ")
        choice.strip()


    nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    while choice == False or choice not in nums or board[int(choice[0]) - 1] != "-":
        display_board()
        print("Sorry, wrong move.")
        choice = input("Your move: ")
        choice.strip()

    board[int(choice[0]) - 1] = symbol
    
    if check_win():
        display_board()
        print("Game over!")
        print("The winner is " + current_player + "!")
        game_on = False
    elif check_tie():
        display_board()
        print("It is a tie!")
        game_on = False

    flip_player()
    

while game_on:
    play()

