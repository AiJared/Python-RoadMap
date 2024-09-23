"""
Write a short program that takes as input three integers, a, b, and c, from
the console and determines if they can be used in a correct arithmetic
formula (in the given order), like “a+ b = c,” “a = b− c,” or “a∗b = c.”
"""

def arithmetic_formula():
    # Getting the three integers via console
    a = int(input("Enter the first integer: "))
    b = int(input("Enter the second integer: "))
    c = int(input("Enter the third integer: "))

    # Check if any of the formalas is correct with the three integers
    if (a +b == c) or (a == b - c) or (a * b == c):
        return True
    else:
        return False

print(arithmetic_formula())