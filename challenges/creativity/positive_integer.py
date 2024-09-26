"""
Write a Python program that can take a positive integer greater than 2 as
input and write out the number of times one must repeatedly divide this
number by 2 before getting a value less than 2
"""

def positive_integer():
    value = int(input("Enter a positive integer greater than 2: "))
    count = 0

    if value > 2:
        while value >= 2:
            value = value / 2
            count += 1
    else:
        print("Please provide a number greater than 2")

    return count

result = positive_integer()
print(f"The number of divisions by 2 before getting a value less than 2 is: {result}")
