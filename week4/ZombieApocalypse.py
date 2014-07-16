"""
Student portion of Zombie Apocalypse mini-project
"""

import random
import poc_grid
import poc_queue
import poc_zombie_gui

# global constants
EMPTY = 0 
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = "obstacle"
HUMAN = "human"
ZOMBIE = "zombie"

class GameQueue(poc_queue.Queue):
    """
    Class implementation of a FIFO queue for Zombie Apocalypse The Game.
    """
    def __init__(self,_item=None):
        self._next = 0
        poc_queue.Queue.__init__(self)
        if _item != None:
            self._items = list(_item)
            
    def remove_item(self,_item):
        """remove element from Queue at extract position"""
        self._items.remove(_item)
    
    def clone(self):
        """ return a copy of current object"""
        return self._items[:]
    
    def set_start(self):
        """set start position of the element"""
        self._next = 0
        
    def has_next(self):
        """return position of element"""
        self._next += 1
        return self._next <= len(self)

class Zombie(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list = None, 
                 zombie_list = None, human_list = None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        self._zombie_list = GameQueue(zombie_list)
        self._human_list = GameQueue(human_list)
       
        
    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        self.__init__(self._grid_height, self._grid_width)

#        def reset(_alllist):
#            """reset all element from _list"""
#            for _list in _alllist:
#                for _row in range(self._grid_height):
#                    for _col in range(self._grid_width):
#                        _list[_row][_col] = EMPTY
#                                            
#        reset([self._cells,self._human_list,self._zombie_list])
           
    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.enqueue((row,col))

                
    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)
          
    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        # replace with an actual generator
        
        return self._zombie_list

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.enqueue((row,col))
        
    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)
    
    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        # replace with an actual generator
       
        return self._human_list
        
    def compute_distance_field(self, entity_type):
        """
        Function computes a 2D distance field
        Distance at member of entity_queue is zero
        Shortest paths avoid obstacles and use distance_type distances
        """
        _visited = self.clone()
        for _row in range(self._grid_height):
            for _col in range(self._grid_width):
                if not self.is_empty(_row,_col):
                    _visited.set_full(_row,_col)
        #print _visited
        _distance_field = [[self._grid_width*self._grid_height for _width in range(self._grid_width)] 
                                            for _height in range(self._grid_height)]
        
        #        for i in _distance_field:
#            print i
        _boundary = GameQueue(self._human_list.clone()) if entity_type == HUMAN \
                                    else GameQueue(self._zombie_list.clone())
        _copy_boundary = _boundary.clone()
        #print _boundary
        while not self.data_empty(_boundary):
            _current_cell  = _boundary.dequeue()
            _visited.set_full(_current_cell[0],_current_cell[1])
            if _current_cell in _copy_boundary:
                _distance_field[_current_cell[0]][_current_cell[1]] = EMPTY
            neighbors = self.four_neighbors(_current_cell[0],_current_cell[1])
            #print _current_cell,_distance_field
            for _neighbor in neighbors:
                
                #print _neighbor
                #if _neighbor not in _visited:
                #print _neighbor
                if _visited.is_empty(_neighbor[0],_neighbor[1]) and _neighbor != _current_cell:
                    #self.set_full(_neighbor[0],_neighbor[1])
                    _visited.set_full(_neighbor[0],_neighbor[1])
                    _distance_field[_neighbor[0]][_neighbor[1]] = _distance_field[_current_cell[0]][_current_cell[1]] if \
                    _distance_field[_current_cell[0]][_current_cell[1]] > self._grid_width + self._grid_height else \
                        _distance_field[_current_cell[0]][_current_cell[1]] + 1                   
                    _boundary.enqueue(_neighbor)
#                    
#        for i in _distance_field:
#            print i
        return _distance_field
                 #   pass

#                    

        
            
    
    def move_humans(self, zombie_distance):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        self._human_list.set_start()
        while self._human_list.has_next():
            _human = self._human_list.dequeue()
            _max = zombie_distance[_human[0]][_human[1]]
            neighbors = self.eight_neighbors(_human[0],_human[1])
            for _row,_col in neighbors:
                if _max < zombie_distance[_row][_col]:
                   _max =  zombie_distance[_row][_col]
                   _human = (_row,_col)
            self._human_list.enqueue(_human)
            
#        for _human in _humans[:]:
#            _humans.remove(_human)
#            neighbors = self.four_neighbors(_human[0],_human[1])
#            _random = random.choice(neighbors)
#            print _random
#            _human = tuple(_random)
#            print _human
            
         
        
    
    def move_zombies(self, human_distance):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        self._zombie_list.set_start()
        _clone_zombies = GameQueue(self._zombie_list.clone())
        while _clone_zombies.has_next():
            _zombie = self._zombie_list.dequeue()
            _min = human_distance[_zombie[0]][_zombie[1]]
            if _zombie not in self._human_list:
                neighbors = self.four_neighbors(_zombie[0],_zombie[1])
                for _row,_col in neighbors:
                    if _min > human_distance[_row][_col]:
                       _min =  human_distance[_row][_col]
                       _zombie = (_row,_col)
            else:
                self._human_list.remove_item(_zombie)
            self._zombie_list.enqueue(_zombie)

            
    def clone(self):
        """ Return a copy Object of current Object"""

        return Zombie(self._grid_height,self._grid_width)
    
    def data_empty(self,_data):
        """ Return a empty list if it haven't any elements"""
        return len(_data) == 0
    
    def __str__(self):
        """
        Return multi-line string represenation for grid
        """
        ans = 'Grid:\n'
        ans += poc_grid.Grid.__str__(self)
        ans += 'Humans:'+str(self._human_list)
        ans += '\nZombies:'+str(self._zombie_list)
       
        return ans

# Start up gui for simulation - You will need to write some code above
# before this will work without errors

#poc_zombie_gui.run_gui(Zombie(30, 40))
#_obj = Zombie(3,3, [], [], [(2, 2)])
#_obj = Zombie(3, 3, [], [(1, 1)], [])
#for i in _obj.compute_distance_field('zombie'):
#    print i 
#_obj = Zombie(20, 30, [(4, 15), (5, 15), (6, 15), (7, 15), (8, 15), (9, 15), (10, 15), (11, 15), (12, 15), (13, 15), (14, 15), (15, 15), (15, 14), (15, 13), (15, 12), (15, 11), (15, 10)], [], [(18, 14), (18, 20), (14, 24), (7, 24), (2, 22)])
#_obj.clear()
#print _obj
#for i in _obj.compute_distance_field(HUMAN):
#    print i
#   
#obj = Zombie(3, 3, [], [(2, 2)], [(1, 1)])
#dist = [[4, 3, 2], [3, 2, 1], [2, 1, 0]]
#print obj.move_humans(dist)
#obj = Zombie(3, 3, [], [(1, 1)], [(2, 2)])
#dist = [[4, 3, 2], [3, 2, 1], [2, 1, 0]]
#obj.move_zombies(dist)
#print obj.zombies() 
#obj = Zombie(3, 3, [], [(1, 1)], [(2, 2)])
#dist = [[4, 3, 2], [3, 2, 1], [2, 1, 0]]
#obj.move_zombies(dist)
#print obj
