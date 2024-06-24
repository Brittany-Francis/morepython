letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
letter_to_points={key:value for key, value in zip (letters, points)}

letter_to_points[" "]=0
print(letter_to_points)

def score_word(word):
  points_total=0
  for let in word:
    if let in letter_to_points:
      points_total+=letter_to_points[let]
    else:
      points_total+=0
  return points_total
brownie_points= score_word("BROWNIE")

print(brownie_points)
player_to_words={"player1":["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader":["ZAP", "COMA", "PERIOD"]}

player_to_points={}

for player in player_to_words:
  player_points=0
  for word in player_to_words[player]:
    player_points+=score_word(word)
  player_to_points[player]=player_points

print(player_to_points)

def play_word(player, word):
  player_to_words[player].extend([word])
  return player_to_words

play_word("player1", "RED")
play_word("wordNerd", "LEMON")
print(player_to_words)

def update_point_totals(dict):
  for player in dict:
    print(player)
    player_points=0
    for word in dict[player]:
      #print(dict[player])
      player_points+=score_word(word)
    player_to_points[player]=player_points
  return player_to_points

point_total=update_point_totals(player_to_words)

print(point_total)