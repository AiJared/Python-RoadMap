"""
Python’s random module includes a function shuffle(data) that accepts a
list of elements and randomly reorders the elements so that each possible order occurs with equal probability. 
The random module includes a 
more basic function randint(a, b) that returns a uniformly random integer
from a to b (including both endpoints). Using only the randint function,
implement your own version of the shuffle function.
"""

# Step by step strategy
"""
1. Start by iterating through the list
2. For each element in the list (at index i) generate a random index j between in and the end of the list.
3. Swap the element at index i with the element at index j
4. Continue this process until all the elements have been shuffled.
"""
