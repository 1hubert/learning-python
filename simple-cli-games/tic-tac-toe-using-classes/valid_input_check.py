def get_length_from_user():
    """Ask user for length."""
    valid_length = False
    user_input = None

    while not valid_length:
        user_input = input('Input length: ')

        try:
            length = float(user_input)
            if length <= 0:
                raise ValueError

            valid_length = True  # if these are succesful, then yay!
        except ValueError:
            print('This is not a valid length. Try again')

    return user_input


def get_length():
    while True:
        user_input = input('length: ')
        
        try:
            length = float(user_input)
            if length <= 0:
                raise ValueError
            break
        except ValueError:
            print('This is not a valid length. Try again.')
    
    return length


"""
1. zmienne dla sprawdzanej wartości i dla poprawności inputu
2. pętla while trwająca do momentu aż otrzymamy poprawny input
    1) pobranie inputu
    2) zamiana inputu na int (jeśli wywali ValueError dostajemy wiadomość o niepoprawnym inpucie)
    3) dowolne inne rzeczy sprawdzające input takie jak przedział wartości, które jeśli się nie zgadzają ręcznie wywołujemy ValueError
    4) jeśli do tego momentu nie mamy ValueError, ustawiamy poprawność inputu na True co kończy pętlę while
"""

a = get_length()
print(a)