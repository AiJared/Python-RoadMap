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