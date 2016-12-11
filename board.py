from ship import Ship

class Board:
    EMPTY = 'O'
    MISS = '.'
    HIT = '*'
    SUNK = '#'  
    board_size = 10
    board = []# the main grid 
    user_input = "a1" # this attricute will hold user input
    board_headers = [] # stores a list of board headers
    vessel_orientation = "h" # by default the orientation is horizontal
    occupied_spots = [] # will be a list of tuples that represent occupied spots on the board
    vessel = ("Patrol Boat",2) # a tuple, by default its a Patrol Boat  
    x = 0 # default value for x is 0
    y = 0 # default value for y is 0
    marker = "" #this represents the action on the board i.e hot, miss , sunk
    
    
    def __init__(self, **kwargs):
      self.starter_board()# creates the board when the class gets initialized
      
      # sets any additional attributes and their values when the  class is initialized
      for key,value in kwargs.items():
        setattr(self,key,value)
        
        
    def starter_board(self):
      #creating the headers for the board
      self.board_headers=[chr(c) for c in range(ord('A'), ord('A') + self.board_size)]
      # crating a 2 D array of empty postion strings i.e [[row],[col]]
      self.board= [[self.EMPTY for c in range(self.board_size)] for _ in range(self.board_size)]
         
    
    def assign_ship_to_board(self):
      """This method loops through around the vessel width.
      Then adds the x and y coordinates to the board and to a list called
      occupied_spots"""
      
      if self.vessel_orientation.lower() == "v": #checking the orientation
        self.marker = Ship.VERTICAL_SHIP
        for i in range(self.vessel[1]):# keep assigning markers based on width of ship
          self.board[self.x+i][self.y]= self.marker # puts the ship at a point on the grid vertically
          self.occupied_spots.append((self.x+i,self.y)) # add the spot to occupied spots
      elif self.vessel_orientation.lower() == "h":#check the orientation
        self.marker = Ship.HORIZONTAL_SHIP
        for i in range(self.vessel[1]):# keep assigning markers based on width of ship
          self.board[self.x][self.y+i]= Ship.HORIZONTAL_SHIP # puts the ship at a point on the grid horizontally
          self.occupied_spots.append((self.x,self.y+i))     

          
    def user_input_to_coordinates(self):
      """ this method takes user input and converts 
      them in a tuple of coordinates"""
      
      # checking the length of the user input string. if its more than 2 than perform the below logic
      if len(self.user_input)==3:
        #someone enters d10. i need to add 1 and 0 and convert to a int
        self.x = int(self.user_input[1]+self.user_input[2]) - 1 
      else:  #else index 1 in the string is ok to use as the x axis 
        # second letter in user input becomes the x axis. -1 is to deal with list starting at 0 index
        self.x = int(self.user_input[1]) -1 
      # first letter in user input is used to grab the index from the headers list
      self.y = self.board_headers.index(self.user_input[0].upper())
      
      
    def is_valid_input(self):
      self.user_input = self.user_input.strip()
      
      # check to see if user input is empty or greater than 3
      if len(self.user_input) < 1 or len(self.user_input)>3:
        return False
      elif len(self.user_input) == 3:
          first_letter = self.user_input[0].upper()# user input representing the board header
          second_letter = self.user_input[1]+self.user_input[2]#when the row is 10 i.e a10 
          if first_letter not in self.board_headers: # if the first letter is not a header on the board
            return False
          elif second_letter not in ["1","2","3","4","5","6","7","8","9","10"]: # second letter doesnt represent a row
            return False
          else:
            return True
      elif len(self.user_input) < 3:
          first_letter = self.user_input[0].upper()
          second_letter = self.user_input[1]
          if first_letter not in self.board_headers: # if the first letter is not a header on the board
            return False
          elif int(second_letter) not in [1,2,3,4,5,6,7,8,9,10]: # second letter doesnt represent a row
            return False
          else:
            return True
      else:
        return True
        
      
    def is_empty_position(self):
      """this method checks to see if the user input can be assigned to
      the board based on wether the spot is empty"""
      
      self.user_input_to_coordinates() # this method will create the x and y coordinates of the board
      
      #check to see if the spot is vacant horizontally and vertically      
      if self.board[self.x][self.y] == self.EMPTY:#
        return True
      else:
        return False
        
    
    def is_valid_position(self):
      """this method checks to see that the width of the ship
      does not exceed the width of the board horizontally or vertically.
      So if a ship is positioned at J1 horizontally and its width is 3
      spaces it doesnt fit on the board"""
      
         
      if self.vessel_orientation != "h": #check the orientation
        #check to see the ship width doesnt exceed the width of the board horizontally
        if (self.board_size - self.x) < self.vessel[1]: 
          return False
        else:
          return True
      else:
        #check to see the ship width doesnt exceed the width of the board vertically
        if (self.board_size - self.y)< self.vessel[1]:
          return False
        else:
          return True
        
        
    def is_overlapping(self):
      """ this method loops around the ships width vertically and horizontally
      and then checks to see if any of the spots in the loop are not vacant.
      So if a ships width is 3 spaces going horizontally placed at A1, the function
      check that B1 and C1 are not occupied by another ship"""
      
      for i in range(self.vessel[1]):
        if self.vessel_orientation == "h":
          if self.board[self.x][self.y+i]!= self.EMPTY: # checking horizontally
            return True # mean the ship is overlapping
            continue
        elif self.board[self.x+i][self.y]!= self.EMPTY:# checking vertically
          return True # mean the ship is overlapping
          continue
        else:
          pass
        
        
    def print_board(self):
      print("   " + " ".join(self.board_headers)) # first prints the headers
      
      row_num = 1
      for mylist in self.board:
        #printing out each list with a number to its right to represent the row
        print(str(row_num).rjust(2) + " " +" ".join(mylist))
        row_num += 1

      

        
      
      
      
      
    
    
    
      
    
          
          

      

        
        
      
      
             
