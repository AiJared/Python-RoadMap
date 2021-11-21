# Try except prevents an error in our python program
# Incase of an error it prevents whatever we want to tell the user7
try:
    x = int(input('Enter an integer: '))
    print(x)
except:
    print('Something went wrong...Please try again!')

# Using except in a specific error for example Valueerror as shown below
try:
    x = int(input('Enter an integer: '))
    print(x)
except ValueError:
    print('Value not an integer!')

# Using else
try:
    x = int(input('Enter an integer: '))
    print(x)
except:
    print('Something went wrong...Please try again!')
else:
    print('nothing went wrong')

# Using finally at the end of the code
try:
    x = int(input('Enter an integer: '))
    print(x)
except:
    print('Something went wrong...Please try again!')
finally:
    print('try except finished')