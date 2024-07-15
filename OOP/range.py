class Range:
    """
    A class that mimics the built-in range class.
    """

    def __init__(self, start, stop=None, step=1):
        """
        Initialize a Range interface.

        Semantics is similar to buit-in range class.
        """

        if step == 0:
            raise ValueError('step cannot be 0')
        
        if stop is None:
            start, stop = 0, start # should be treated as if range(0, n)

        # calculate the effective length once
        self._length = max(0, (stop - start + step -1) // step)
        
        # need knowlwdge of start and step (but not stop) to support __getitem__
        self._start = start
        self._step = step
