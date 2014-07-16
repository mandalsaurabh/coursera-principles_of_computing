"""
Clone of 2048 game.
"""

import poc_2048_gui
import random
# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}
   
def merge(line):
    """
Helper function that merges a single row or column in 2048
"""
    # replace with your code
    lists = line[:]
    nexts = 0
    while nexts < len(lists) - 1:
        check = True
        for i in range(nexts+1,len(lists)):
            if (lists[nexts]==lists[i] or lists[nexts]==0) and check:
                if lists[nexts] != 0:
                    check = False
                lists[nexts] +=lists[i]
                lists[i] = 0
            elif lists[nexts]!=lists[i] and lists[i]!=0:
                check = False
        nexts+=1
    return lists
            

    

class TwentyFortyEight:
    """
Class to run the game logic.
"""

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self.row = grid_height
        self.col = grid_width
        self.grid = [ [0 if i==j else 0 for i in range(self.col)] for j in range (self.row)]
    def reset(self):
        """
Reset the game so the grid is empty.
"""
        # replace with your code
        self.grid = [ [0 if i==j else 0 for i in range(self.col)] for j in range (self.row)]
        
    def __str__(self):
        """
Return a string representation of the grid for debugging.
"""
        # replace with your code
        return "%s\n%s\n%s\n%s\n" % (self.grid[0],self.grid[1],self.grid[2],self.grid[3])

    def get_grid_height(self):
        """
Get the height of the board.
"""
        # replace with your code
        return self.row
    
    def get_grid_width(self):
        """
Get the width of the board.
"""
        # replace with your code
        return self.col
                            
    def move(self, direction):
        """
Move all tiles in the given direction and add
a new tile if any tiles moved.
"""
        # replace with your code
        clone = self.clone(self.grid[:])
        if direction in [UP,DOWN]:
            for i in range(self.col):
                line = [k[i] for k in self.grid]
                if direction in [DOWN]:
                    line.reverse()
                lists = merge(line)
                if direction in [DOWN]:
                    lists.reverse()
                for j in range(self.row):
                    self.set_tile(j,i,lists[j])
        elif direction in [LEFT,RIGHT]:
            for i in range(self.row):
                line = self.grid[i]
                if direction in [RIGHT]:
                    line.reverse()
                lists = merge(line)
                if direction in [RIGHT]:
                    lists.reverse()
                for j in range(self.col):
                    self.set_tile(i,j,lists[j])
        #print self.is_change(clone,self.grid[:])
        if(not self.is_over() and clone!=self.grid ):
            self.new_tile()


        
    def new_tile(self):
        """
Create a new tile in a randomly selected empty
square. The tile should be 2 90% of the time and
4 10% of the time.
"""
        # replace with your code
        rad = random.randint(1,100)
        print self.grid
        empty_index = random.choice([(i,j) for i in range(self.row)
                       for j in range(self.col) if self.grid[i][j] == 0])
        value = 2 if rad > 10 else 4
        self.set_tile(empty_index[0],empty_index[1],value)
        
        
    def set_tile(self, row, col, value):
        """
Set the tile at position row, col to have the given value.
"""
        # replace with your code
        
        self.grid[row][col] = value
        
    def get_tile(self, row, col):
        """
Return the value of the tile at position row, col.
"""
        # replace with your code
        return self.grid[row][col]
    
    def is_over(self):
        """
check the value of grid if it haven't value 0,Game is Over
"""
        return len(filter(lambda x: 0 in x ,self.grid)) == 0
    
    def clone(self,value):
        """
copy all value of grid into a new variable and return it
"""
        clone = [ [0 for i in range(self.col)] for j in range (self.row)]
        for i in range(self.row):
            for j in range(self.col):
                clone[i][j] = self.grid[i][j]
        return clone
    
    
 
    
poc_2048_gui.run_gui(TwentyFortyEight(4, 5))
