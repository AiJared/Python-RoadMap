"""
Write a Python program that repeatedly reads lines from standard input
until an EOFError is raised, and then outputs those lines in reverse order
(a user can indicate end of input by typing ctrl-D).
"""
def inputvalue():
    lines = []
    print("Enter input (ctr-D) to stop: ")

    try:
        # Keep reading until EOFError
        while True:
            line = input()
            lines.append(line)
    
    except EOFError:
        # Print the lines in reverse order
        for line in reversed(lines):
            print(lines)

inputvalue()