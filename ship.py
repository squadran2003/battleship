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
  
  
  
  def __init__(self,**kwargs):
        
    for key,item in kwargs.items():
      setattr(self,key,value)
    