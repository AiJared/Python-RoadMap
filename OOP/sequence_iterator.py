class SequenceIterator:
    """
    An iterator for any Python's sequence types.
    """

    def __init__(self, sequence):
        """
        Create an iterator for the given sequence.
        """
        self._seq = sequence # keep a reference to the underlying data
        self._k = -1 # will increment to 0 on the first call to nec

    def __next__(self):
        """
        Return the next element or else raise StopIteration error.
        """  
        self._k += 1 # advance to the next index
        if self._k < len(self._seq):
            return self._seq[self._k] # return the data element
        else:
            raise StopIteration()
        
    def __iter__(self):
        """
        By convention, an iterator must return itself as an iterator.
        """
        return self
    