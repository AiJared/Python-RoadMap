class Vector:
    """
    Represents a vector in a multidimensional space.
    """
    def __init__(self, d):
        """
        Create d-dimensional vector of zeros.
        """
        self._coords = [0] * d

    def __len__(self):
        """
        Return the dimension of the vector.
        """
        return self._coords
    
    def __getitem__(self, j):
        """
        Return the jth coordinate of vector.
        """
        return self._coords[j]
    
    def __setitem__(self, j, val):
        """
        Set jth coordinate of vector to given value.
        """
        self._coords[j] = val

    def __add__(self, other):
        """
        Return sum of two vectors.
        """
        if len(self) != len(other):
            raise ValueError('dimensions must agree!')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        
        return result
    
    def __eq__(self, other):
        """
        Return True if vector has same coordinates as others.
        """
        return self._coords == other._coords
    
    def __ne__(self, other):
        """
        Return True if vector differs from other.
        """
        return not self == other # relies on existing __eq__
    
    def __str__(self):
        """
        Produce string representation of vector.
        """
        return '<' + str(self._coords)[1:-1] + '>'

v = Vector(5)
print(v) # construct a 5D vector <0,0,0,0,0>
v[1] = 23 # <0,23,0,0,0> (based on the __setitem__ method)
v[-1] = 45 # also via __setitem__
print(v[4]) # via __getitem__
u = v + v # <0,46,0,0,90> via __add__
print(u)
total = 0

for entry in v: # implicit iteration via __len__ and __getitem__
    total += entry