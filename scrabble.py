'''
Scrabble

In this project, you will process some data from a group of friends playing scrabble. 
You will use dictionaries to organize players, words, and points.
'''

# Two lists of letters and their corresponding points
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Create dictionary with letters as keys and points as values
letters_to_points = {key: value for key, value in zip(letters, points)}
print(letters_to_points)
# {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 4, 'O': 1, 'P': 3, 'Q': 10, 
# 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10}

# Our letters list did not take into account blank tiles. Let's fix that 
letters_to_points[' '] = 0

# Update letters_to_points so it can also handle lowercase inputs:
letters_to_points.update({key.lower(): value for key, value in letters_to_points.items()})
print(letters_to_points)
# {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 4, 'O': 1, 'P': 3, 'Q': 10, 
# 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10, ' ': 0, 'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 
# 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 4, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 
# 'y': 4, 'z': 10}

# Function that will take a word and return how many points it is worth
def score_word(word):
  point_total = 0
  for letter in word:
    # Use get method to provide default value of 0 if letter is not in letters_to_points.
    point_total += letters_to_points.get(letter, 0)
  return point_total

brownie_points = score_word('BROWNIE')
print(brownie_points)
# 15

# Create dictionary with players and a list of words they have played
player_to_words = {'player1': ['BLUE', 'TENNIS', 'EXIT'], 'wordNerd': ['EARTH', 'EYES', 'MACHINE'], 'Lexi Con': ['ERASER' ,'BELLY' ,'HUSKY'],  
                   'Prof Reader': ['ZAP', 'COMA', 'PERIOD']}
print(player_to_words)
# {'player1': ['BLUE', 'TENNIS', 'EXIT'], 'wordNerd': ['EARTH', 'EYES', 'MACHINE'], 'Lexi Con': ['ERASER', 'BELLY', 'HUSKY'], 
# 'Prof Reader': ['ZAP', 'COMA', 'PERIOD']}

# Create a dictionary with players as keys and the point total of their words played as values
player_to_points = {}

# Function to update player_to_points dictionary with each players score
def update_point_totals():
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
    player_to_points[player] = player_points

# Test out update point total function
update_point_totals()
print(player_to_points)
# {'player1': 29, 'wordNerd': 32, 'Lexi Con': 31, 'Prof Reader': 31}

# Function to add words to players word list, append new players and update the point total of each player
def play_word(player, word):
  if player not in player_to_words:
    # Add new player
    player_to_words[player] = []
  player_to_words[player].append(word)
  # Update point total
  update_point_totals()

# Player1 plays the word Peacock
play_word('player1', 'Peacock')
# New player 'Lizzo' plays 'JUICE 
play_word('Lizzo', 'JUICE')

print(player_to_words)
# {'player1': ['BLUE', 'TENNIS', 'EXIT', 'Peacock'], 'wordNerd': ['EARTH', 'EYES', 'MACHINE'], 'Lexi Con': ['ERASER', 'BELLY', 'HUSKY'], 
# 'Prof Reader': ['ZAP', 'COMA', 'PERIOD'], 'Lizzo': ['JUICE']}
print(player_to_points)
# {'player1': 46, 'wordNerd': 32, 'Lexi Con': 31, 'Prof Reader': 31, 'Lizzo': 14}
