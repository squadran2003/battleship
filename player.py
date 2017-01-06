class Player():
  name = None
  player_type = 1
  board = None # holds on to an instance called board
  guess_board = None # holds on to an instance called guess_board
  guesses = [] # holds on to name of the ship guessed

  
  def __init__(self,**kwargs):
    self.guesses = []
    self.get_player_name()
    Player.player_type+=1
       
    for key,value in kwargs.items():
      setattr(self,key,value)
      
      
  def get_player_name(self):
    """this method take 1 argument, type of player i.e 
    uses that to display the prompt. i.e your name player1 or
    your name player2 etc"""
    
    self.name = input("player{} what is your name >>  ".strip().format(str(self.player_type)))
    if self.name == "":
      self.get_player_name()
  


      

    