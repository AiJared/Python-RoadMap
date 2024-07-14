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
        