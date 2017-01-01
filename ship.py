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
  x = 0 # default value for x is 0
  y = 0 # default value for y is 0
  orientation = "h" # by default the orientation is horizontal
  vessel = ("Patrol Boat", 2) # a tuple, by default its a Patrol Boat  
  
  
     
      
  def ship_orientation(self):
    self.orientation = input("Is it horizontal? (Y)/N: " ).lower()
    if self.orientation =="y":
      return "h"
    if self.orientation == "n":
      return "v"
    else:
      return ""
    