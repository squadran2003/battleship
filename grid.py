from ship import Ship

class Grid:
  headers = []
  grid = []
  grid_size = 10

  
  def create_grid(self):
  	  # cannot use chr(a) as unicode gets messed up in windows console
      self.headers=["A","B","C","D","E","F","G","H","I","J"]
      # crating a 2 D array of empty postion strings i.e [[row],[col]]
      self.grid= [[Ship.EMPTY for c in range(self.grid_size)] for _ in range(self.grid_size)]
      
      
  def print_board(self):
    print(" "+" "+" "+" ".join(self.headers)) # first prints the headers
    
    row_num = 1
    for mylist in self.grid:
      #printing out each list with a number to its right to represent the row
      print(str(row_num).rjust(2) + " " +" ".join(mylist))
      row_num += 1
      

