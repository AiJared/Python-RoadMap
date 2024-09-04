"""
Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution
"""

def minmax(data):
    # Start with the first number as both minimum and maximum
    smallest = largest = data[0]

    # Iterate through the sequence to find the actual minimum and maximum numbers
    for num in data:
        if num < smallest:
            smallest = num # Update smallest if the minimum number is found
        if num > largest:
            largest = num  # Update largest if the maximum number is found
    return (smallest, largest)

print(minmax([1,2,3,4]))