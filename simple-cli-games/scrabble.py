letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {letters:points for letters, points in zip(letters, points)}

letter_to_points.update({" ": 0})

def score_word(word):
  point_total = 0
  supa_string = "("
  for letter in word:
    if word[0] == letter:
      point_total += letter_to_points.get(letter.upper(), 0)
      supa_string += str(letter_to_points.get(letter.upper(), 0))
    else:
      point_total += letter_to_points.get(letter.upper(), 0)
      supa_string += " + " + str(letter_to_points.get(letter.upper(), 0))
  supa_string += ") = " + str(point_total)
  return point_total

brownie_points = score_word("brownie")

print(brownie_points)

player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

player_to_points = {}

def play_word(player, word):
  prev_words = player_to_words.get(player, [])
  player_to_words[player] = prev_words + [word]
  update_point_totals()
  print(player_to_points)
  
def update_point_totals():
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
    player_to_points[player] = player_points
  

play_word("player1", "cat")
play_word("player2", "dog")
play_word("player1", "elephant")
play_word("player2", "tiger")