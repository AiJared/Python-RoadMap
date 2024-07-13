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
    
    