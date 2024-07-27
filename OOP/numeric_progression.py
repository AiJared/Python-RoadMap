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