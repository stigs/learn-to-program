# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """

    
    # Write your Rat methods here.

    def __init__(self, symbol, row, col):
        """ (Rat, str, int, int) --> NoneType

        A Rat with a name/symbol and a position on the grid of (row, col)

        >>> paul = Rat(RAT_2_CHAR, 1, 4)
        >>> paul.symbol
        'P'
        >>> paul.row
        1
        >>> paul.col
        4
        >>> paul.num_sprouts_eaten
        0
        
        """

        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0

    def __str__(self):
        """(Rat) -> str
        Return a string representation of this Rat.

        >>> paul = Rat('P', 1, 4)
        >>> print(paul)
        P at (1, 4) ate 0 sprouts.

        """
        return '{0} at ({1}, {2}) ate {3} sprouts.'.format(self.symbol, \
                self.row, self.col, self.num_sprouts_eaten)


    def set_location(self, row, col):
        """ (Rat, int, int) --> NoneType
        Moves the Rat to a new row and column location

        >>> paul = Rat('P', 1, 4)
        >>> paul.set_location(2, 4)
        >>> paul.row
        2
        >>> paul.col
        4
        """
        self.row = row
        self.col = col

    def eat_sprout(self):
        """ (Rat) --> NoneType
        Adds 1 to the Rat's num_sprouts_eaten

        >>> paul = Rat('P', 1, 4)
        >>> paul.eat_sprout()
        >>> paul.num_sprouts_eaten
        1
        >>> paul.eat_sprout()
        >>> paul.num_sprouts_eaten
        2
        
        """
        self.num_sprouts_eaten = self.num_sprouts_eaten + 1
        
    


    
class Maze:
    """ A 2D maze. """

    # Write your Maze methods here.

    def __init__(self, map, rat_1, rat_2):
        """(Maze, list of list of str, Rat, Rat) --> NoneType

        Creates the maze from a list of lists of str representing each row of the maze and \
        creates rat1 and rat2, placing them in the maze.

        >>> my_maze = Maze([['#', '#', '#', '#', '#', '#', '#'], \
                              ['#', '.', '.', '.', '.', '.', '#'], \
                              ['#', '.', '#', '#', '#', '.', '#'], \
                              ['#', '.', '.', '@', '#', '.', '#'], \
                              ['#', '@', '#', '.', '@', '.', '#'], \
                              ['#', '#', '#', '#', '#', '#', '#']], \
                            Rat('J', 1, 1), \
                            Rat('P', 1, 4))
        
        >>> print(my_maze.rat_2)
        P at (1, 4) ate 0 sprouts.

        >>> print(my_maze.num_sprouts_left)
        3
        """

        self.maze = map
        self.rat_1 = rat_1
        self.rat_2 = rat_2

        # Put the rat symbols into the maze map
        self.maze[self.rat_1.row][self.rat_1.col] = self.rat_1.symbol
        self.maze[self.rat_2.row][self.rat_2.col] = self.rat_2.symbol
        
        self.num_sprouts_left = 0
        for i in range(len(self.maze)):
            self.num_sprouts_left = self.num_sprouts_left + self.maze[i].count(SPROUT)

    def is_wall(self, row, col):
        """ (Maze, int, int) -> bool

        Returns true if and only if the character at the row and col is a wall character or 

        Precondition:
        The number of rows must be <= the number of rows in the maze and \
        the number of columns must be <= the number of columns of the maze \
        row <= len(my_maze.maze) and col <= len(my_maze.maze[0])

        >>> my_maze = Maze([['#', '#', '#', '#', '#', '#', '#'], \
                              ['#', '.', '.', '.', '.', '.', '#'], \
                              ['#', '.', '#', '#', '#', '.', '#'], \
                              ['#', '.', '.', '@', '#', '.', '#'], \
                              ['#', '@', '#', '.', '@', '.', '#'], \
                              ['#', '#', '#', '#', '#', '#', '#']], \
                            Rat('J', 1, 1), \
                            Rat('P', 1, 4))
                            
        >>> my_maze.is_wall(0,0)
        True
        >>> my_maze.is_wall(1,2)
        False
        
        """

        if self.maze[row][col] == WALL:
            return True
        else:
            return False
    
    def get_character(self, row, col):
        """(Maze, int, int) -> str
        Returns a str representation of the object at the given row and col in the Maze

        Precondition:
        The number of rows must be <= the number of rows in the maze and \
        the number of columns must be <= the number of columns of the maze \
        row <= len(my_maze.maze) and col <= len(my_maze.maze[0])
        
        >>> my_maze = Maze([['#', '#', '#', '#', '#', '#', '#'], \
                              ['#', '.', '.', '.', '.', '.', '#'], \
                              ['#', '.', '#', '#', '#', '.', '#'], \
                              ['#', '.', '.', '@', '#', '.', '#'], \
                              ['#', '@', '#', '.', '@', '.', '#'], \
                              ['#', '#', '#', '#', '#', '#', '#']], \
                            Rat('J', 1, 1), \
                            Rat('P', 1, 4))
                            
        >>> my_maze.get_character(0,0)
        'WALL'

        >>> my_maze.get_character(1,2)
        'HALL'

        >> my_maze.get_character(4,1)
        'SPROUT'

        >>> my_maze.get_character(1,4)
        'P'

        >>> my_maze.get_character(10,6)
        'This position is outside of the map boundaries. Please provide a row that is 6 or less and a column that is 7 or less.'

        """
        
        if row <= len (self.maze) and col <= len(self.maze[0]):
            if self.rat_1.row == row and self.rat_1.col == col:
                return self.rat_1.symbol
            elif self.rat_2.row == row and self.rat_2.col == col:
                return self.rat_2.symbol
            elif self.is_wall(row,col):
                return 'WALL'
            elif self.maze[row][col] == HALL:
                return 'HALL'
            elif self.maze[row][col] == SPROUT:
                return 'SPROUT'
        else:
            return 'This position is outside of the map boundaries. '\
                    'Please provide a row that is {0} or less and a column ' \
                    'that is {1} or less.'.format(len(self.maze), len(self.maze[0]))

    def move(self, rat, v, h):
        """ (Maze, Rat, int, int) -> bool

        Returns true if and only if there isn't a wall in the way and changes a rat's vertical position by v and horizontally by h

        >>> my_maze = Maze([['#', '#', '#', '#', '#', '#', '#'], \
                              ['#', '.', '.', '.', '.', '.', '#'], \
                              ['#', '.', '#', '#', '#', '.', '#'], \
                              ['#', '.', '.', '@', '#', '.', '#'], \
                              ['#', '@', '#', '.', '@', '.', '#'], \
                              ['#', '#', '#', '#', '#', '#', '#']], \
                            Rat('J', 1, 1), \
                            Rat('P', 3, 1))

        >>> my_maze.move(my_maze.rat_2, DOWN, NO_CHANGE)
        True
        >>> my_maze.rat_2.row
        4
        >>> my_maze.rat_2.col
        1
        >>> my_maze.rat_2.num_sprouts_eaten
        1

        >>> my_maze.move(my_maze.rat_1, NO_CHANGE, RIGHT)
        True
        >>> my_maze.rat_1.row
        1
        >>> my_maze.rat_1.col
        2
        >>> my_maze.rat_1.num_sprouts_eaten
        0

        >>> my_maze.move(my_maze.rat_2, DOWN, NO_CHANGE)
        False
        >>> my_maze.rat_2.row
        4
        >>> my_maze.rat_2.col
        1
        >>> my_maze.rat_2.num_sprouts_eaten
        1
        """

        # Move the rat horizontally and vertically if and only if there is not a wall in front of it.
        if not self.is_wall(rat.row, rat.col + h) and not self.is_wall(rat.row + v, rat.col):

            # Change the current location back to a hallway and move the rat to the new location.
            self.maze[rat.row][rat.col] = HALL
            rat.set_location(rat.row + v, rat.col + h)
        

            
            # Check to see if there is a sprout at the new position, and if there is, eat it and modify the maze map
            if self.maze[rat.row][rat.col] == SPROUT:
                rat.eat_sprout()
                self.maze[rat.row][rat.col] = HALL
                self.num_sprouts_left = self.num_sprouts_left - 1

            return True

        else:
            return False

    def __str__(self):
        """ (Maze) -> str

        Prints a str representation of the Maze and the status of the rats

        >>> my_maze = Maze([['#', '#', '#', '#', '#', '#', '#'], \
                              ['#', '.', '.', '.', '.', '.', '#'], \
                              ['#', '.', '#', '#', '#', '.', '#'], \
                              ['#', '.', '.', '@', '#', '.', '#'], \
                              ['#', '@', '#', '.', '@', '.', '#'], \
                              ['#', '#', '#', '#', '#', '#', '#']], \
                            Rat('J', 1, 1), \
                            Rat('P', 1, 4))

        >>> print(my_maze)
        #######
        #J..P.#
        #.###.#
        #..@#.#
        #@#.@.#
        #######
        J at (1, 1) ate 0 sprouts.
        P at (1, 4) ate 0 sprouts.
        
        """
        row = ''

        
        
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):

                if i == self.rat_1.row and j == self.rat_1.col:
                    row = row + self.rat_1.symbol
                elif i == self.rat_2.row and j == self.rat_2.col:
                    row = row + self.rat_2.symbol
                else: 
                    row = row + self.maze[i][j]
            row = row + '\n'

        row = row + str(self.rat_1) + '\n' + str(self.rat_2)
        return row
                

## To Do:
## 
## 3) Remove tests from paul and jess into self.rat_1 and self.rat_2
if __name__ == '__main__':

    import doctest
    doctest.testmod()
