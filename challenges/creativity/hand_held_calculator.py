"""
Write a Python program that simulates a handheld calculator. 
Your program should process input from the Python console representing buttons
that are “pushed,” and then output the contents of the screen after each operation is performed. 
Minimally, your calculator should be able to process
the basic arithmetic operations and a reset/clear operation.
"""
# Steps

"""
The simulated hand held calculator in the program below can handle basic arithmetic operations
(addition, subtraction, multiplication, division). The program will take user inputs representing
the buttons pushed (numbers and operators) and display results after each operation.
1. Users enter button presses as strings(e.g. 5 + 3 * 2)
2. The calculator evaluates the inputs after user presses the "Enter" key.
3. The user can type "c" or "clear" to reset the calculator.
"""
def calculator():
    print("Welcome to the simulated hand held calculator.")
    print("Type 'C' or 'clea'r to reset the calculator or exit to quit.")

    # Intialize an empty expression
    expression = ""