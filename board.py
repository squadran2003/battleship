from ship import Ship
from grid import Grid

class Board(Grid,Ship):
    board_input = ""
    board_errors = []
    # will be a list of coordinates
    occupied_spots = [] 
    # list of dicts. each dict will have a coord and its corresponding ship name
    ships_on_board = []
    x =  0
    y = 0
    
    
    def __init__(self, **kwargs):
      # creates the grid on the board when the class gets initialized.
      # this method is inherited from the Grid class
      self.create_grid()
      self.occupied_spots = []
      self.ships_on_board = []
           
      # sets any additional attributes and their values on initialization
      for key,value in kwargs.items():
        setattr(self,key,value)
        
        
    def assign_ship_to_board(self):
      """This method loops through around the vessel width.
      Then adds the x and y coordinates to the board and based 
      on orientation, it then adds to a lists called occupied_spots and the other
      ships_on_board. ships_on_board is a list of dictionaries with coord for keys
      and aircraft name for values. This is later used as a reference for adding the sunk
      marker on the guess board"""
            
      for i in range(self.vessel[1]):
        if self.orientation == "v":
          # puts the ship at a point on the grid vertically
          self.grid[self.x+i][self.y]= self.VERTICAL_SHIP 
          # add the spot to occupied spots
          self.occupied_spots.append((self.x+i,self.y)) 
          # keeping track of ships and their coords
          self.ships_on_board.append({(self.x+i,self.y):self.vessel[0]}) 
        else:
          # puts the ship at a point on the grid horizontally
          self.grid[self.x][self.y+i]= Ship.HORIZONTAL_SHIP 
          self.occupied_spots.append((self.x,self.y+i))
          self.ships_on_board.append({(self.x,self.y+i):self.vessel[0]})
          
    
    def is_empty_position(self):
      """this method checks to see if the user input can be assigned to
      the board based on wether the spot is empty"""
      
      # this method sets the boards x and y coordinates
      self.set_board_coordinates()
      
      #check to see if the spot is vacant horizontally and vertically      
      if self.grid[self.x][self.y] == self.EMPTY: 
        return True
      elif self.grid[self.y][self.x] == self.EMPTY:
        return True
      else:
        return False
        
    
    def is_valid_position(self):
      """this method checks to see that the width
      of the ship does not exceed the width of the 
      board horizontally or vertically.So if a ship 
      is positioned at J1 horizontally and its width 
      is 3 spaces it doesnt fit on the board"""
      
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
      """ this method loops around the ships width
      vertically and horizontally and then checks to 
      see if any of the spots in the loop are not vacant.
      So if a ships width is 3 spaces going horizontally 
      placed at A1, the function check that B1 and C1 are 
      not occupied by another ship"""
      
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
        
    
    def set_board_coordinates(self):
      """ this method takes board input and converts 
      them in a tuple of coordinates. user input a1 becomes 
      (0,0) and so on"""
        
      # checking the length of the user input string. 
      #if its more than 2 than perform the below logic
      if len(self.board_input)==3:
        #someone enters d10. i need to add 1 and 0 and convert to a int
        self.x = int(self.board_input[1]+self.board_input[2]) - 1 
      #else index 1 in the string is ok to use as the x axis 
      else:  
        # second letter in user input becomes the x axis
        self.x = int(self.board_input[1]) -1 
      # first letter in user input is used to grab the index from the headers list
      self.y = self.headers.index(self.board_input[0].upper())
      
    
    def validate_board_input(self):
      """this method return a boolean based on the input the board
      receives, if input is less than 2 or greater than 3 the input 
      is invalid.If a person enters a13, again is invalid as there 
      is only 10 rows on the board"""
           
      rows = [1,2,3,4,5,6,7,8,9,10]
      # check to see if user input is less than 2 or greater than 3
      if len(self.board_input) < 2 or len(self.board_input) > 3:
        return False
      elif len(self.board_input) == 3:
        # user input representing the board header
        first_letter = self.board_input[0].upper()
        # if the first letter is not a header on the board
        if first_letter not in self.headers: 
          return False
        else:
          # try to convert the input to an integer
          try:
            #when the row is 10 i.e a10 
            second_letter = int(self.board_input[1]+ self.board_input[2])
          except ValueError:
            return False
          # second letter doesnt represent a row
          if second_letter not in rows: 
            return False
          else:
            return True
      else:
          first_letter = self.board_input[0].upper()
          second_letter = int(self.board_input[1])
          # if the first letter is not a header on the board
          if first_letter not in self.headers: 
            return False
          # second letter doesnt represent a row
          elif int(second_letter) not in rows: 
            return False
          else:
            return True
          
          
    def validate_board_placement(self):
      """ This method takes the board as an argument
      and validates positions on the that board.
      It checks to see if a spot is empty, checks to
      see if ships are overlapping or that a ship's width
      doesnt exceed the width of the board"""
      
      if self.is_empty_position():
        if self.is_valid_position():
          if self.is_overlapping():
            self.board_errors.append("Your choice of {} is "
                                      "overlapping with another" 
                                     " ship!"
                                    .format(self.board_input))
            return False
          else:
            return True
            
        else:
          self.board_errors.append("Your choice of {}"
                                   " causes the ship to "
                                    " not fit on the board!"
                                   " try another spot"
                                   " or a different orientation"
                                  .format(self.board_input))
          return False
          
      else:
        self.board_errors.append("{}! well that"
                                 " spot is already"
                                  " taken!".format(self.board_input))
        return False     
      
        

      

        
      
      
      
      
    
    
    
      
    
          
          

      

        
        
      
      
             
