"""
Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution
"""

def minmax(data):
    
    smallest = largest = data[0]

    for num in data:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    return (smallest, largest)

print(minmax([1,2,3,4]))