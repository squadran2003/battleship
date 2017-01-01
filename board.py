from ship import Ship
from grid import Grid

class Board(Grid,Ship):
    board_input = ""
    board_errors = []
    occupied_spots = [] # will be a list of dicts where key is the coordinates and value is the ship name
    x =  0
    y = 0
    orientation = None
    
    def __init__(self, **kwargs):
      self.create_grid()# creates the board when the class gets initialized
      self.occupied_spots = []

      
      
      # sets any additional attributes and their values when the  class is initialized
      for key,value in kwargs.items():
        setattr(self,key,value)
        
        
    def assign_ship_to_board(self):
      """This method loops through around the vessel width.
      Then adds the x and y coordinates to the board and based 
      on orientation, it then adds to a list called occupied_spots"""
      
      for i in range(self.vessel[1]):
        if self.orientation == "v":
          self.grid[self.x+i][self.y]= self.VERTICAL_SHIP # puts the ship at a point on the grid vertically
          self.occupied_spots.append((self.x+i,self.y)) # add the spot to occupied spots
        else:
          self.grid[self.x][self.y+i]= Ship.HORIZONTAL_SHIP # puts the ship at a point on the grid horizontally
          self.occupied_spots.append((self.x,self.y+i))

          
    def is_empty_position(self):
      """this method checks to see if the user input can be assigned to
      the board based on wether the spot is empty"""
      
      self.get_board_coordinates()
      
      #check to see if the spot is vacant horizontally and vertically      
      if self.grid[self.x][self.y] == self.EMPTY or self.grid[self.y][self.x] == self.EMPTY:#
        return True
      else:
        return False
        
    
    def is_valid_position(self):
      """this method checks to see that the width of the ship
      does not exceed the width of the board horizontally or vertically.
      So if a ship is positioned at J1 horizontally and its width is 3
      spaces it doesnt fit on the board"""
      
         
      if self.orientation != "h": #check the orientation
        #check to see the ship width doesnt exceed the width of the board horizontally
        if (self.grid_size - self.x) < self.vessel[1]: 
          return False
        else:
          return True
      else:
        #check to see the ship width doesnt exceed the width of the board vertically
        if (self.grid_size - self.y)< self.vessel[1]:
          return False
        else:
          return True
        
        
    def is_overlapping(self):
      """ this method loops around the ships width vertically and horizontally
      and then checks to see if any of the spots in the loop are not vacant.
      So if a ships width is 3 spaces going horizontally placed at A1, the function
      check that B1 and C1 are not occupied by another ship"""
      
      for i in range(self.vessel[1]):
        if self.orientation == "h":
          if self.grid[self.x][self.y+i]!= self.EMPTY: # checking horizontally
            return True # mean the ship is overlapping
            continue
        elif self.grid[self.x+i][self.y]!= self.EMPTY:# checking vertically
          return True # mean the ship is overlapping
          continue
        else:
          pass
        
    
    def get_board_coordinates(self):
      """ this method takes user input and converts 
      them in a tuple of coordinates. user input a1 becomes 
      (0,0) in terms of coordinates"""
      
  
      # checking the length of the user input string. if its more than 2 than perform the below logic
      if len(self.board_input)==3:
        #someone enters d10. i need to add 1 and 0 and convert to a int
        self.x = int(self.board_input[1]+self.board_input[2]) - 1 
      else:  #else index 1 in the string is ok to use as the x axis 
        # second letter in user input becomes the x axis. -1 is to deal with list starting at 0 index
        self.x = int(self.board_input[1]) -1 
      # first letter in user input is used to grab the index from the headers list
      self.y = self.headers.index(self.board_input[0].upper())
      
    
    def validate_board_input(self):
           
      rows = [1,2,3,4,5,6,7,8,9,10]
            
      # check to see if user input is empty or greater than 3
      if len(self.board_input) < 2 or len(self.board_input) > 3:
        return False
      elif len(self.board_input) == 3:
          first_letter = self.board_input[0].upper()# user input representing the board header
          second_letter = int(self.board_input[1])+int(self.board_input[2])#when the row is 10 i.e a10 
          if first_letter not in self.headers: # if the first letter is not a header on the board
            return False
          elif second_letter not in rows: # second letter doesnt represent a row
            return False
          else:
            return True
      else:
          first_letter = self.board_input[0].upper()
          second_letter = int(self.board_input[1])
          if first_letter not in self.headers: # if the first letter is not a header on the board
            return False
          elif int(second_letter) not in rows: # second letter doesnt represent a row
            return False
          else:
            return True
        

      

        
      
      
      
      
    
    
    
      
    
          
          

      

        
        
      
      
             
