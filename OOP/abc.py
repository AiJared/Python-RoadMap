from abc import ABCMeta, abstractmethod

class Sequence(metaclass=ABCMeta):
    """
    Our own version of collections.Sequence abstract base class.
    """

    @abstractmethod
    def __len__(self):
        """
        Return the length of the sequence.
        """

    @abstractmethod
    def __getitem__():
        """
        Return the element at index j of the sequence.
        """

    def __contains__(self, val):
        """
        Retrun True if val is found in the sequence; False otherwise.
        """

        for j in range(len(self)):
            if self[j] == val: # found match
                return True
        return False
    
    def index(self, val):
        """
        Return leftmost index at which val is found (or raise ValueError.)
        """

        for j in range(len(self)):
            if self[j] == val:
                return j
            raise ValueError("Value in Sequence") # never found a match

    def count(self, val):  
        """
        Return the number of elements equal to given value.
        """ 
        
        k = 0
        for j in range(len(self)):
            if self[j] == val:
                k += 1
        return k