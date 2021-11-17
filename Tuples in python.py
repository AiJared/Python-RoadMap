# Tuples are used to store multiple items in a single variable
# Tuples are immutable meaning that you cannot change a value in a tuple
three_numbers = (1, 2, 3)
print(three_numbers)

# Get the first value using the index method
print(three_numbers[0])
 # Tuples allow repetition of values
three_numbers = (1, 2, 3, 1)
print(three_numbers)

# Get the length of a tuple
print(len(three_numbers))

# Check the type
print(type(three_numbers))

# Tuples allows various data types
strings = ('home', 'land', 'earth')
print(strings)

boo = (True, False, True)
print(boo)

three_numbers = (1, 'Home', True, 3, 1)
print(three_numbers)

# Check the data type of a single value of a tuple
print(type(three_numbers[0]))

# Create a tuple using a tuple constructor
three_numbers = tuple((1, 'Home', True, 3, 1))
print(three_numbers)