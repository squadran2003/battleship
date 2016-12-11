from player import Player
from ship import Ship
from board import Board
import os

class Battleship:
  EMPTY = 'O'
  MISS = '.'
  HIT = '*'
  SUNK = '#' 
  player_count = 2
  board_errors = []# this list hold on to an errors that might be raised during validation
  
  
  def set_up(self):
    board1 = Board()
    board2 = Board()
    board3 = Board()
    board4 = Board()
    player2_board2 = Board()
    self.player1 = Player(board1=board1, guess_board=board2)
    self.player2 = Player(board1=board3, guess_board=board4)
  
  
  def __init__(self):
    self.set_up()
    
    
  def assign_ship(self, player, board, ship):
    self.board_errors = []
    board.print_board()
    print("*"*10)
    board.user_input = input("{} where would you like to " 
                                    "place the {} >>".format(player.name, ship)
                                   )
    
    board.vessel_orientation = self.ship_orientation()
    
    if board.vessel_orientation == "":
      self.clear_screen()
      print("Sorry what is your orientation!")
      print("*"*10)
      self.assign_ship(player, board, ship)
    else:
      board.vessel = ship
      if self.validate_board_placement(player):
        board.assign_ship_to_board()
      else:
        self.clear_screen()
        print("*"*10)
        print(self.board_errors[0])# print any errors in the board_errors list 
        self.assign_ship(player, board, ship)

  
  def validate_board_placement(self, player):
    """ this method validates user input, checks if a spot is empty
    and checks if a ship overlaps another"""
    
    if player.board1.is_valid_input():
      if player.board1.is_empty_position():
        if player.board1.is_valid_position():
          if player.board1.is_overlapping():
            self.board_errors.append("Sorry that ship is overlapping!")
            return False
          else:
            return True
            
        else:
          self.board_errors.append("Sorry the ship doesnt fit on the board!")
          return False
          
      else:
        self.board_errors.append("Sorry that spot was taken try again!")
        return False
    else:
      self.board_errors.append("Try again did'nt recognise your input."
                               "Example: a2 where a is the board header"
                               "and 2 is board row!")
      return False
      
    
  def start_placing_ships(self,player):
    print("*"*10)
    for ship in Ship.SHIP_INFO:
      self.clear_screen()
      self.assign_ship(player, player.board1, ship)
    print("*"*10)
    
    
  
  def guess_ship(self, player, board, ships):
    for ship in ships:
      board.user_input = input("{} guess where oponents "
                               "{} is located: a7 >> ".format(player.name, ship[0]))
      board.user_input_to_coordinates()
      if (board.x,board.y) in player.occupied_spots:
        player.hit_points +=1
        player.guesses.append((board.x,board.y))
        board.board[board.x][board.y]="*"
      else:
        player.guesses.append((board.x,board.y))
        board.board[board.x][board.y]="."
      board.print_board()
      
                               
  def get_player_name(self,typeofplayer):# typepfplayer is a string version of the player i.e "player1"
    """this method asks the user for input, checks 
    to see it not blank and return the userinput in this case the name"""
    
    name = input("{} what is your name >> ".format(typeofplayer))
    if name == "":
      print("{} please enter your name >> ".format(typeofplayer))
    else:
      return name
    
  
  def ship_orientation(self):
    orientation = input("Is it horizontal? (Y)/N: " ).lower()
    if orientation =="y":
      return "h"
    if orientation == "n":
      return "v"
    else:
      return ""
    

  def main(self):

    self.player1.name = self.get_player_name("player1")
    # first player starts placing his ships
    self.start_placing_ships(self.player1)
    self.clear_screen()
    input("Press enter to continue")
    self.clear_screen()
    self.player2.name = self.get_player_name("player2")
    #second player starts placing his ships
    self.start_placing_ships(self.player2)
    input("Press enter to continue")

    # allow player 1 to guess where player 2 ships are and visa versa
    for i in range(self.player_count):
      i+=1
      if i < 2:
        self.guess_ship(self.player1, self.player1.guess_board, Ship.SHIP_INFO)
        input("press any key to continue")
      else:
        self.guess_ship(self.player2, self.player2.guess_board, Ship.SHIP_INFO)
    # print 2 boards where oponent has guessed and the current guess
    # if the player has entered a spot they have already guesses prompt them 
      # tell them why their guess was not acceptable, in this case already guesses
    # continue the game untill all of the players ships have been sunk

     
  def clear_screen(self):
    try:
    	os.system('cls')
    except:
    	os.system('clear')
    
   
battlegame = Battleship()
battlegame.main()
