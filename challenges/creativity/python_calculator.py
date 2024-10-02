"""
Write a Python program that can simulate a simple calculator, using the
console as the exclusive input and output device. That is, each input to the
calculator, be it a number, like 12.34 or 1034, or an operator, like + or =,
can be done on a separate line. After each such input, you should output
to the Python console what would be displayed on your calculator.
"""

def calculator():
    firstnum = float(input("Enter the first number: "))
    operator = input("Enter an operator: ")
    secondnum = float(input("Enter the second number: "))

    if operator == "+":
        print(firstnum + secondnum)
    elif operator == "-":
        print(firstnum - secondnum)
    elif operator == "/":
        print(firstnum / secondnum)
    elif operator == "*":
        print(firstnum * secondnum)
    else:
        return "Invalid Operator!"
calculator()