"""
Write a Python program that can “make change.” Your program should
take two numbers as input, one that is a monetary amount charged and the
other that is a monetary amount given. It should then return the number
of each kind of bill and coin to give back as change for the difference
between the amount given and the amount charged. The values assigned
to the bills and coins can be based on the monetary system of any current
or former government. Try to design your program so that it returns as
few bills and coins as possible.
"""

# How the problem will be solved
"""
The Python program below calculates change in US currency which includes bill and coins.
The program will return the change in each type of bill or coin with a goal of minimizing
the amount of bills and coins.

The denominations are:
1. Bills: 100 dollar, 50 dollar, 20 dollar, 10 dollar and 5 dollar
2. Coins: 25 cents(quater), 10 cents(dime), 5 cents(nickle), 1 cent(penny)

The program calculates the change based on the difference between the amount given and the 
amount charged.
"""