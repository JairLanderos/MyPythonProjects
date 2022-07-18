############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


##################### Program starts here #######################
import random
import os
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

new_game = "Y"

while new_game == "Y":
  os.system('clear')
  
  #Print welcome message
  print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
  print(art.logo)
  print("\t\t\t\t  WELCOME TO THE BLACKJACK GAME")
  print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
  
  #Deal both user and computer a starting hand of 2 random card values.
  user_cards = []
  computer_cards = []
  for card in range(2):
    user_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))
  
  print("\n\nThese are your cards:")
  for card in range(2):
    art.draw_card(user_cards[card])
  
  print("\n\nThese are the computer cards:")
  art.draw_card(computer_cards[0])
  art.draw_card_hidden()
  
  print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*\n")
  
  blackjack = False
  if sum(computer_cards) == 21:
    blackjack = True
    winner = False
  elif sum(user_cards) == 21:
    blackjack = True
    winner = True
  
  game_over = False
  if not blackjack:
    #User
    user_cards_number = 2
    hit = "Y"
    while hit == "Y" and sum(user_cards) != 21:
      print(f"Your score is {sum(user_cards)}")
      hit = input("Would you like another card?  Type 'Y' or 'N'\t\t")
      if hit == "Y":
        user_cards.append(random.choice(cards))
        user_cards_number += 1
        print("\nThis is your new card:")
        art.draw_card(user_cards[user_cards_number - 1])
        if sum(user_cards) > 21:
          game_over = True
          break
      else:
        break
  
    print("\n~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*\n")
  
    #Computer
    if game_over == False:
      computer_cards_number = 2
      while sum(computer_cards) < 16:
        computer_cards.append(random.choice(cards))
        computer_cards_number += 1
        print("Computer picks a new card:")
        art.draw_card(computer_cards[computer_cards_number - 1])
      print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*\n")
    
    print(f"Your score is {sum(user_cards)}.")
    print(f"Computer's score is {sum(computer_cards)}.")
    if not game_over and (sum(computer_cards) > 21 or sum(user_cards) > sum(computer_cards)):
      print("YOU WIN!!!")
    elif not game_over and not sum(computer_cards) > 21 and sum(user_cards) == sum(computer_cards):
      print("IT'S A TIE!!!")
    else:
      print("YOU LOSE!!!")
  
    print("\n\nComputer's secret card was:")
    art.draw_card(computer_cards[1])
      
  else:
    if winner:
      print("YOU HAVE BLACKJACK. YOU WIN!!!")
    else:
      print("COMPUTER HAS BLACKJACK. YOU LOSE!!!")
      print("Computer's secret card was:")
      art.draw_card(computer_cards[1])

  print("\n~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*\n")
  new_game = input("Would you like to play again?  Type 'Y' or 'N'\t\t")
