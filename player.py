class Player():
  name = ""
  board = None # holds on to an instance of Board
  guesses = []

  
  def __init__(self,**kwargs):
    self.guesses = []

       
    for key,value in kwargs.items():
      setattr(self,key,value)
      
      
  def get_player_name(self, typeofplayer):
    """this method take 1 argument, type of player i.e 
    uses that to display the prompt. i.e your name player1 or
    your name player2 etc"""
    
    self.name = input("{} what is your name >> ".strip().format(typeofplayer))
  


      

    