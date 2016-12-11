import random

from ship import Ship
from board import Board

class Player(Board):
  
  name = ""
  board1 = None 
  guess_board = None
  hit_points = 0
  guesses = []
  
  
  def __init__(self,**kwargs):
    
    
    for key,value in kwargs.items():
      setattr(self,key,value)
      
  
  def attack(self):
    ran_x = randomn.randint(0,self.board.board_size) # random x coordinate
    ran_y = randomn.randint(0,self.board.board_size) # random y coordinate
    return (ran_x,ran_y)
  
  
  def __str__(self):
    return self.name
    