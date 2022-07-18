import random
import os
from hangman_words import word_list

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False

#Number of lives the user has to guess the word
lives = 6

#Select a letter from the list
chosen_word = random.choice(word_list)
print(f"Welcome to the Hangman game!!!\n\n")

#Create a list with blank spaces to be the game display
display = []
for letter in range(0, len(chosen_word)):
  display += "_"
print(stages[6 - lives])
print(display)

while "_" in display and end_of_game == False:

  #Ask the user for a valid letter
  guess = ""
  while len(guess) != 1:
    guess = input("Guess a leter:  ").lower()
    if len(guess) != 1:
      print("You must guess only one letter. Try again\n\n")

  #CLear the screen
  os.system('clear')
  
  #Check if the user guess matches a letter from the chosen word
  isRight = False
  for position in range(len(chosen_word)):
    if guess == chosen_word[position]:
      display[position] = guess
      isRight = True

  #Feedback to the user. A life is substracted if wrong
  if isRight == False:
    lives -= 1
    print(f"Wrong! You have {lives} lives left\n\n")
  else:
    print(f"Right! You have {lives} lives left\n\n")

  #Check if user has ran out of lives to stop the game
  if lives == 0:
      end_of_game = True

  #Print the current stage and the game display
  print(stages[6 - lives])
  print(display)
    

if end_of_game == True:
  print("\n\nYOU LOSE!!")
else:
  print("\n\nYOU WIN!!")
