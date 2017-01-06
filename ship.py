class Ship:
  
  SHIP_INFO = [
    ("Aircraft Carrier", 5),
    ("Battleship", 4),
    ("Submarine", 3),
    ("Cruiser", 3),
    ("Patrol Boat", 2)
]
  VERTICAL_SHIP = '|'
  HORIZONTAL_SHIP = '-'
  EMPTY = 'O'
  MISS = '.'
  HIT = '*'
  SUNK = '#'
  orientation = "h" # by default the orientation is horizontal
  vessel = ("Patrol Boat", 2) # a tuple, by default its a Patrol Boat  
  
  
  def get_ship_orientation(self):
    user_input = input("Is it horizontal? (Y)/N: " ).lower()
    if user_input =="":
      print("What is your orientation !!")
      self.get_ship_orientation()
    elif user_input=="y":
      self.orientation = "h"
    else:
      self.orientation = "v"
