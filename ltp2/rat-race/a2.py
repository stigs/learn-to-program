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

        >>> paul = Rat('P', 1, 4)
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

        >>> map = [['#', '#', '#', '#', '#', '#', '#'], \
              ['#', '.', '.', '.', '.', '.', '#'], \
              ['#', '.', '#', '#', '#', '.', '#'], \
              ['#', '.', '.', '@', '#', '.', '#'], \
              ['#', '@', '#', '.', '@', '.', '#'], \
              ['#', '#', '#', '#', '#', '#', '#']]
        >>> jess = Rat('J', 1, 1),
        >>> paul = Rat('P', 1, 4)
        >>> my_maze = Maze(map, jess, paul)
        >>> map == my_maze.maze
        True
        >>> print(maze_1.rat_2)
        P at (1, 4) ate 0 sprouts.
        
        """

        self.maze = map
        self.rat_1 = rat_1
        self.rat_2 = rat_2
    
    def get_character(self, row, col):
        """(Maze, int, int) -> str
        Returns a str representation of the object at the given row and col in the Maze

        Precondition:
        The number of rows must be <= the number of rows in the maze and \
        the number of columns must be <= the number of columns of the maze
        row <= len(my_maze.maze) and col <= len(my_maze.maze[0])
        
        >>> get_character(0,0)
        WALL

        >>> get_character(1,1)
        HALL

        >>> get_character(1,4)
        P at (1, 4) ate 0 sprouts.

        """
        #Need to start working here.

if __name__ == '__main__':

    import doctest
    doctest.testmod()
