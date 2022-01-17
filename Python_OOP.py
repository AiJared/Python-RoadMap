import math

class Point:
    'Represents a point in two dimensional geometric coordinates'

    def __init__(self, x=0, y=0):
        '''Initializes the position of a new point. The x and y coordinates can be specified
        . If they are not, the point defaults to the origin.'''
        self.move(x, y)

    def move(self, x, y):
        "Move the point to a new location in 2D space"
        self.x = x
        self.y = y
    
    def reset(self):
        'Reset the point back to the geometric origin: 0, 0'
        self.move(0, 0)

    def calculate_distance(self, other_point):
        """Calculate distance from this point to a second 
        point passed as a parameter
        
        This Function uses the pythagorean theorem to calculate the diatance between
        the two points. The distance is 
        returned as a float."""
        return math.sqrt(
            (self.x - other_point.x) ** 2 +
            (self.y - other_point.y) ** 2)