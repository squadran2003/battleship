## battleship
command line version of the famous battleship game

## The clear screen method 
  
  ```python

  # if the script is run in the console change

  def clear_screen(self):
    print("\033c", end="")
  
  # to

  import os

  def clear_screen(self):
  	try:
	  os.system('cls')
	except:
	  os.system('clear')

  ```

## To run the game
   run the script battleship.py


