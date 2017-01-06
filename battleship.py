from player import Player
from ship import Ship
from board import Board


class Battleship(Ship):
     
  def set_up(self):
    #creating two instances of the board class for player1 and player2
      # one will hold the board where the ships are placed and the other visual
      # representation of the guesses
    self.player1 = Player(board=Board(), guess_board=Board())
    self.clear_screen()
    input("Press any key to continue")
    self.clear_screen()
    self.player2 = Player(board=Board(), guess_board=Board())
  
  
  def __init__(self):
    self.set_up()
  
  
  def get_board_input(self, player, board_number , msg):
    """ this method takes 3 arguments. player, board_number
    and msg. board_number 1 = board, board_number 2= guess_board,
    msg is the input message to the player"""
    
    print("*"*10)
    board = None
    if board_number == 1:
      player.board.board_input = input(msg)
    else:
      player.guess_board.board_input = input(msg)  
    
    
  
  def assign_ship(self, player, ship):
    """this method takes a player and a ship,
    requests board input, and orientation. Validates the
    input and if valid assigns the ship to the board"""
    
    player.board.board_errors = []
    player.board.print_board()
    self.get_board_input(player, 1 ,"{} place your {} " 
                         "on the board.for "
                         "e.g a1 is top left >> "
                         .format(player.name, ship[0])
                          )

    if player.board.validate_board_input():
      player.board.get_ship_orientation()
      if player.board.validate_board_placement():
        player.board.vessel = ship
        player.board.assign_ship_to_board()
          
      else:
        self.clear_screen()
        print("*"*10)
        # print any errors in the board_errors list 
        print(player.board.board_errors[0])
        print("*"*10)
        self.assign_ship(player, ship)
    else:
      player.board.board_errors.append("Try again did'nt recognise"
                                       " your input. An example would"
                                       " be: a2, where a is the board header"
                                        " and 2 is board row!")
      self.clear_screen()
      # print any errors in the board_errors list
      print(player.board.board_errors[0]) 
      print("*"*10)
      self.assign_ship(player, ship)
  
  
     
  def place_each_ship(self,player):
    print("*"*10)
    for ship in self.SHIP_INFO:
      self.clear_screen()
      self.assign_ship(player, ship)
    print("*"*10)
    
    
  def guess_ship(self, guessing_player, opponent):
    print("Hit[*], Miss[.], Sunk ship[#]")
    self.get_board_input(opponent, 2 , "{}, select"
                                   " a location"
                                   " to shoot at >> "
                                   "".format(guessing_player.name))  

    if opponent.guess_board.validate_board_input():
      # creates the x and y coord for the guess board
      opponent.guess_board.set_board_coordinates()
      x, y = opponent.guess_board.x, opponent.guess_board.y
      #check if a spot has already been guessed
      if self.duplicate_guess((x,y), opponent):
        print("Sorry you have already guessed that spot")
        # ask again for input
        self.guess_ship(guessing_player, opponent)
      else:
        #keep a record of the spot guessed
        opponent.guess_board.occupied_spots.append((x,y))
        # check if a ship has been hit
        if self.has_ship_been_hit(opponent, (x,y)):
          self.ship_hit(guessing_player, opponent, (x,y))
        else:
          self.ship_miss(opponent, (x,y))
        #check to see if any ships have sunk
        self.check_ship_sunk(opponent, guessing_player)
    else:
      print("Sorry did not recognise your input!!")
      self.guess_ship(guessing_player, opponent)
      

  def get_ship_name(self,opponent,coord):
    """this method takes an opponent and coordinates,
    its loops around the ships_on_board list on the 
    opponents main board. This list a list of dictionaries 
    with coordinates for keys and aircraftname for values"""
    
    for mydict in opponent.board.ships_on_board:
      for key,val in mydict.items():
        if key == coord:
          # the val is the aircraftname
          return val
        else:
          pass
        
  
  def ship_hit(self, guessing_player, opponent, coords):
    #board_index this value is used to pop the tuple out
    board_index = opponent.board.occupied_spots.index(coords)
    # name of the ship
    ship_name = self.get_ship_name(opponent, coords)
    # keep a record of what ship was hit
    guessing_player.guesses.append(ship_name)
    # add marker to the board
    self.add_guess_markers(opponent, coords, Ship.HIT)
    # A hit has occured remove the tuple from the occupied_spots
    opponent.board.occupied_spots.pop(board_index)  
    print("Yayy you hit a ship!!")
    input("press any key to continue")
    
  
  def ship_miss(self, opponent, coords):
    # add marker to the board
    self.add_guess_markers(opponent, coords, Ship.MISS)
    print("Yayy you missed !!")
    input("press any key to continue")
    
  
  
  
  def duplicate_guess(self, coord, opponent):
    """this method checks if coord are in the 
        board.occupied_spots if it is it means the 
        guessing_player has already tried to guess 
        that spot"""
    
    if coord in opponent.guess_board.occupied_spots:
      return True
    else:
      return False
    
    
  def add_guess_markers(self, opponent, coords, marker):
    """ this method adds the hit or miss markers 
    to the coordinates on to the guess_board and 
    main board"""
    
    x,y = coords
    opponent.guess_board.grid[x][y] = marker
    opponent.board.grid[x][y] = marker
    
  
  def add_sunk_markers(self, opponent, mylist2):
    """ this method loops around the passed in list
    and adds the sunk marker to the guess_board and main board.
    The list contains coordinates"""
    
    for coord in mylist2:
      x,y = coord
      opponent.board.grid[x][y]= self.SUNK
      opponent.guess_board.grid[x][y]= self.SUNK
      
  
  def get_ship_coordinates(self,opponent, shipname):
    """this method takes the opponent and shipname.
    its loops around the dictionary and return all 
    the coordinates for that ship"""
    
    coords = []
    for mydict in opponent.board.ships_on_board:
      for key,val in mydict.items():
        if val == shipname:
          coords.append(key)
        else:
          pass
    return coords

  
    
  def start_guessing(self, guessing_player, opponent):
      self.clear_screen()
      print("Your opponents board")
      print("*"*10)
      opponent.guess_board.print_board()
      print("*"*10)
      print("Your board")
      print("*"*10)
      guessing_player.board.print_board()
      print("*"*10)
      self.guess_ship(guessing_player, opponent)
      print("*"*10)
      
  
  def check_ship_sunk(self, opponent, guessing_player):
    """ check the number of times each aircraft 
    name appears in the guessing_players guesses,
    based on that add the appropriate markers"""
    
    if guessing_player.guesses.count("Aircraft Carrier")== 5:
      self.add_sunk_markers(opponent, 
                            self.get_ship_coordinates(
                                opponent, "Aircraft Carrier"
                                )
                           )
    if guessing_player.guesses.count("Battleship")== 4:
      self.add_sunk_markers(opponent, 
                            self.get_ship_coordinates(
                                opponent, "Battleship")
                              )
    if guessing_player.guesses.count("Submarine")== 3:
      self.add_sunk_markers(opponent, 
                            self.get_ship_coordinates(
                                opponent, "Submarine")
                           )
    if guessing_player.guesses.count("Cruiser")== 3:
      self.add_sunk_markers(opponent, 
                            self.get_ship_coordinates(
                                opponent, "Cruiser")
                           )
    if guessing_player.guesses.count("Patrol Boat")== 2:
      self.add_sunk_markers(opponent, 
                            self.get_ship_coordinates(
                                opponent, "Patrol Boat")
                           )
    else:
      pass
      
      

  def has_ship_been_hit(self, opponent, coord):
    """this method takes an opponent and coordinates
    of the guess. It check to see if the coordiante is
    in the dictionary. if it is its a hit"""
    
    if coord in opponent.board.occupied_spots:
      return True
    else:
      return False
      
  
  def print_game_over(self, player):
    print("Game Over")
    print("*"*10)
    print("{} you win".format(player.name))
      
  
  def play(self,player):
      # player starts placing his ships
      self.place_each_ship(player)
      self.clear_screen()
      
  
  def clear_screen(self):
    print("\033c", end="")
    
    
  def main(self):
    self.play(self.player1)
    self.clear_screen()
    input("Press enter to continue")
    self.clear_screen()
    self.play(self.player2)
    input("Press enter to continue")
        
    while True:
      if len(self.player2.board.occupied_spots) == 0:
        self.print_game_over(self.player1)
        break
      elif len(self.player1.board.occupied_spots) == 0:
        self.print_game_over(self.player2)
        break
      else:
        self.start_guessing(self.player1, self.player2)
        self.start_guessing(self.player2, self.player1)
        


        
battlegame = Battleship()
battlegame.main()
