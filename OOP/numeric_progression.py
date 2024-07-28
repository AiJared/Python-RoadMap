class Progression:
    """
    Iterator producing generic progression.
    Default iterator produces the whole numbers 0,1,2.
    """
    def __init__(self, start = 0):
        """
        Initialize current to the first value of the progression
        """
        self._current = start

    def _advance(self):
        """
        Update self._current to a new value.

        This should be overridded by a subclass to customize progression.
        
        By convetion, if current is set to None, this designates the
        end of a finite progression.
        """
        self._current += 1

    def __next__(self):
        """
        Return the next element, or railse StopIteration error.
        """
        if self._current is None: # our convention to end a progression
            raise StopIteration() 
        else:
            answer = self._current # record current value to return
            self._advance() # advance to prepare for next time
            return answer # return the answer
        
    def __iter__(self):
        """
        By convention, an iterator must return itself as an iterator.
        """
        return self
    
    def print_progression(self, n):
        """
        Print next n values of the progression.
        """
        print(' '.join(str(next(self)) for j in range(n)))

class ArithmeticProgression(Progression):
    """
    Iterator producing an arithmetic progression.
    """

    def __init__(self, increment=1, start=0):
        """
        Creates a new arithmetic progression.

        increment the fixed constant to add to each term (default 1)
        start     the first term of the progression (default 0)
        """

        super().__init__(start) # initialize the base class
        self._increment = increment

    def _advance(self):
        """
        Update the current value by adding the fixed increment
        """
        self._current += self._increment

class GeometricProgression(Progression):
    """
    Iterator producing a geometric progression.
    """

    def __init__(self, base=2, start=1):
        """
        Creates a new geometric progression.

        base    the fixed constant multiplied to each term (default 2)
        start   the first term of the progression (default 1)
        """

        super().__init__(start)
        self._base = base