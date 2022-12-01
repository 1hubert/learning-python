import random


class Card:
    def __init__(self, card_color, card_type):
        self.color = card_color
        self.type = card_type

    def __str__(self):
        return f'{self.type} {self.color}'


class CardGame:
    def __init__(self):
        self.deck = []
        self.card_colors = ['Spade', 'Club', 'Diamond', 'Heart']
        self.card_types = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def prepare_deck(self, deck_type='52'):
        """Makes sure the deck is empty and fills it with cards based on type of deck. Shuffles the deck at the end.
        Type argument possible values: 52, 9+"""

        min_card_type_idx = None
        if deck_type == '52':
            min_card_type_idx = 0
        elif deck_type == '9+':
            min_card_type_idx = 7
        else:
            print('Incorrect \"type\" value. Excpected values: {\"52\", \"9+\"}')
            raise ValueError
        
        for card_type in self.card_types[min_card_type_idx:]:
            for card_color in self.card_colors:
                self.deck.append(Card(card_color=card_color, card_type=card_type))

        random.shuffle(self.deck)

        return self.deck

    def show_deck(self):
        for card in self.deck:
            print(f'{card.type} {card.color}')

    def represent_card(self, card):
        return f'{card.type} {card.color}'


class Blackjack(CardGame):
    def __init__(self):
        super().__init__()
        self.prepare_deck()
        self.points_per_card = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'K': 10, 'Q': 10, 'A': 11}
        self.player_hand = [self.deck.pop(), self.deck.pop()]
        self.dealer_hand = [self.deck.pop()]
        self.dealer_points = self.hand_points(self.dealer_hand)
        self.player_points = self.hand_points(self.player_hand)

    def represent_hand(self, hand):
        represented_hand = ''
        for card in hand:
            represented_hand += f'{card.type} {card.color} '

        return represented_hand
    
    def hand_points(self, hand):
        total_points = 0
        ace_in_hand = False

        for card in hand:
            total_points += self.points_per_card[card.type]
            if card.type == 'A':
                ace_in_hand = True
        
        if ace_in_hand and total_points > 21:
            total_points = total_points - 11 + 1

        return total_points

    def show_current_table(self):
        dealers_hand = self.represent_hand(self.dealer_hand)
        self.dealer_points = self.hand_points(self.dealer_hand)

        players_hand = self.represent_hand(self.player_hand)
        self.player_points = self.hand_points(self.player_hand)

        print('Dealer\'s hand:')
        print(f'{dealers_hand} ({self.dealer_points} points)', end='\n\n')

        print('Player\'s hand:')
        print(f'{players_hand} ({self.player_points} points)', end='\n\n')

    def dealer_turn(self):
        """Adds cards to dealer until his points >=17, reveals the victorious one."""
        while self.hand_points(self.dealer_hand) <= 17:
            self.dealer_hand.append(self.deck.pop())
        
        self.show_current_table()

    def hit(self):
        new_card = self.deck.pop()
        self.player_hand.append(new_card)
        print(f'You got {new_card}')

    def double_down(self):
        pass

    def split(self):
        pass


def play_blackjack():
    bj = Blackjack()

    if bj.player_points == 21:
        print('Blackjack!!')

    while bj.hand_points(bj.player_hand) < 21:
        bj.show_current_table()
        
        user_input = None
        possible_choices = ['hit', 'stand']
        while user_input not in possible_choices:
            user_input = input('What ya do: ')

        if user_input == 'hit':
            bj.hit()
        elif user_input == 'stand':
            break
    
    bj.player_points = bj.hand_points(bj.player_hand)
    if bj.player_points == 21:
        bj.show_current_table()
        print('You are VICTORIOUS :tada:')
    elif bj.player_points > 21:
        bj.show_current_table()
        print('Busted. You lose :(')
    else:
        bj.dealer_turn()
        if bj.player_points > 21:
            print('Busted. You lose :(')
        elif bj.hand_points(bj.dealer_hand) > 21:
            print('Dealer busts. You win!!')
        elif bj.player_points > bj.dealer_points:
            print('You are VICTORIOUS :tada:')
        elif bj.player_points < bj.dealer_points:
            print('You lose and the dealer wins.')
        else:
            print('Remis')


play_blackjack()
