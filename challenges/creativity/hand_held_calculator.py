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

    while True:
        # Take input from the user
        user_input = input("Enter number, operator(+,-,*,/) or C to clear: ").strip().lower()
    
        # Check if user wants to exit the calculator
        if user_input == "exit":
            print("Exiting the calculator. Goodbye!")
            break
        elif user_input == "c" or user_input == "clear":
            expression = ""
            print("Calculator reset. Enter new expression.")
        else:
            # Add the input to current expression
            expression += user_input

            try:
                # Evaluate the current expression and show the result
                result = eval(expression)
                print(f"Current expression: {expression} = {result}")
            except (SyntaxError, ZeroDivisionError, NameError):
                print("Invalid input or error in expression. Please try again.")
                expression = "" # reset the expression or error

calculator()  