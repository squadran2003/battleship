from player import Player
from ship import Ship
from board import Board
import os

class Battleship(Ship):
  player_count = 2
  
  
  def set_up(self):
    #creating two instances of the board class for player1 
    self.player1 = Player(board=Board(), guess_board=Board())
    #creating two instances of the board class for player2 
    self.player2 = Player(board=Board(), guess_board=Board())
  
  
  def __init__(self):
    self.set_up()
    
    
  def assign_ship(self, player, ship):
    """this method takes a player and a ship,
    requests board input, orientation. Validates the input and if valid assigns
    the ship to the board"""
    
    
    player.board.board_errors = []
    player.board.print_board()
    print("*"*10)
    player.board.board_input = input("{} where would you like to " 
                                    "place the {} >>".format(player.name, ship)
                                   )

    if player.board.validate_board_input():
      player.board.orientation = self.ship_orientation()
      if player.board.orientation == "":
        self.clear_screen()
        print("Sorry what is your orientation!")
        print("*"*10)
        self.assign_ship(player, ship)
      else:
        if self.validate_board_placement(player.board):
          player.board.vessel = ship
          player.board.assign_ship_to_board()
          
        else:
          self.clear_screen()
          print("*"*10)
          print(player.board.board_errors[0])# print any errors in the board_errors list 
          self.assign_ship(player, ship)
    else:
      player.board.board_errors.append("Try again did'nt recognise your input."
                               "An example would be: a2, where a is the board header"
                               "and 2 is board row!")
      self.clear_screen()
      print(player.board.board_errors[0])# print any errors in the board_errors list  
      self.assign_ship(player, ship)
  
  
  def validate_board_placement(self, board):
    """ This method validates positions on the board.
    It checks to see if a spot is empty, checks to see if ships are
    overlapping or that a ship width doesnt exceed the width of the
    board"""
    
    if board.is_empty_position():
      if board.is_valid_position():
        if board.is_overlapping():
          board.board_errors.append("Sorry that ship is overlapping!")
          return False
        else:
          return True
          
      else:
        board.board_errors.append("Sorry the ship doesnt fit on the board!")
        return False
        
    else:
      board.board_errors.append("Sorry that spot was taken try again!")
      return False

      
    
  def place_each_ship(self,player):
    print("*"*10)
    for ship in self.SHIP_INFO:
      self.clear_screen()
      self.assign_ship(player, ship)
    print("*"*10)
    
    
  
  def guess_ship(self, guessing_player, opponent):
    opponent.guess_board.board_input = input("{}, select a location"
                                             " to shoot at > ".format(guessing_player.name))
    
    if opponent.guess_board.validate_board_input():
      
      opponent.guess_board.get_board_coordinates()# creates the x and y coord for the guess board
      if (opponent.guess_board.x,opponent.guess_board.y)in opponent.guess_board.occupied_spots:
        print("You already guessed that spot!!")
        self.guess_ship(guessing_player, opponent)
      else:
        # if the guess is in the main board its a hit
        if (opponent.guess_board.x,opponent.guess_board.y) in opponent.board.occupied_spots:
          # added the correct guess to the guess_board occupied spots to prevent same spot being guessed again
          opponent.guess_board.occupied_spots.append(
                        (opponent.guess_board.x,opponent.guess_board.y)
                                                     )
          # pop the coord out of the main board if guessed correctly
          opponent.board.occupied_spots.pop(opponent.board.occupied_spots.index(
              (opponent.guess_board.x,opponent.guess_board.y)
                                            ))
          # add the guess to the guessing players guesses
          guessing_player.guesses.append((opponent.guess_board.x,opponent.guess_board.y))
          # add the hit marker to the spot on the opponents main board
          opponent.board.grid[opponent.guess_board.x][opponent.guess_board.y]= self.HIT
           # add the hit marker to the spot on the opponents guess board
          opponent.guess_board.grid[opponent.guess_board.x][opponent.guess_board.y]= self.HIT
          print("*"*10)
          print("Yaay you hit a ship!!")
          input("Press any key to continue")
        else:
          # unsuccesful hit
          guessing_player.guesses.append(
                      (opponent.guess_board.x,opponent.guess_board.y)
                                          )
          # add the miss marker to the spot on the opponents main board
          opponent.board.grid[opponent.guess_board.x][opponent.guess_board.y]= self.MISS
           # add the miss marker to the spot on the opponents guess board
          opponent.guess_board.grid[opponent.guess_board.x][opponent.guess_board.y]= self.MISS
          print("*"*10)
          print("You missed!!")
          input("Press any key to continue")
    else:
      print("Sorry did not recognise your input!!")
      self.guess_ship(guessing_player, opponent)
      

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
      
  
  def print_game_over(self, player):
      print("Game Over")
      print("*"*10)
      print("{} you win".format(player.name))
      
  
  def validate_name(self,player):
    if player.name == "":
      return False
    else:
      return True
      
  
  def play(self,player, playertype):
    player.get_player_name(playertype)
    if self.validate_name(player):
      # player starts placing his ships
      self.place_each_ship(player)
      self.clear_screen()
    else:
      self.clear_screen()
      # no name given, call play() again
      self.play(player,playertype)
      
  
  def clear_screen(self):
    try:
    	os.system('cls')
    except:
    	os.system('clear')
    
  
  def board_error(self,msg):
    self.clear_screen()
    print(msg)
    print("*"*10)    
  
  
  def main(self):
    self.play(self.player1, "player1")
    self.clear_screen()
    input("Press enter to continue")
    self.clear_screen()
    self.play(self.player2, "player2")
    input("Press enter to continue")
        
    while True:
      # if no player1 ships remaining. player2 wins and visa vera
      if len(self.player1.board.occupied_spots) < 1:
        self.print_game_over(self.player2)
        break
      elif len(self.player2.board.occupied_spots) < 1:# if no player2 ships remaining. player1 wins
        self.print_game_over(self.player1)
        break
      else:
        self.start_guessing(self.player1, self.player2)
        self.start_guessing(self.player2, self.player1)
        


        
    
battlegame = Battleship()
battlegame.main()
