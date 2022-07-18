import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

symbols = ["♣", "♦", "♥", "♠"]
cards_letters = ["J", "Q", "K"]

symbols

def draw_card(number):
  symbol = random.choice(symbols)
  if len(str(number)) == 1:
    print(f"""
  .-------.
  |{number}      |
  |{symbol}      |
  |       |
  |      {symbol}|
  |      {number}|
  `-------'
  """)
  else:
    if number == 10:
      letter = random.choice(cards_letters)
      print(f"""
  .-------.
  |{letter}      |
  |{symbol}      |
  |       |
  |      {symbol}|
  |      {letter}|
  `-------'
  """)
    else:
      print(f"""
  .-------.
  |A      |
  |{symbol}      |
  |       |
  |      {symbol}|
  |      A|
  `-------'
  """)

def draw_card_hidden():
  print(f"""
  .-------.
  |*******|
  |*******|
  |*******|
  |*******|
  |*******|
  `-------'
  """)
                   

                                      
     
