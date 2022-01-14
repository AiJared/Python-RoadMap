# There are two types of functions: Those that perfom a task and those that do calculations and return a value
def greet(first_name, last_name): # A parameter is the input defined inside a function (first_name and last_name are our parameters)
    print(f'Hi {first_name} {last_name}')
    print('Welcme aboard')


greet('Mosh', 'Hamedani') # An argument is the actual value returned (Mosh and Hamedani are our arguments)
greet('Jared', 'Otieno')

def get_greeting(name):
    return f'Hi {name}'
message = get_greeting('Jared')
print(message)

# Keyword Arguments
# Keyword Arguments makes code more easily readable
def increment(number, by):
    return number + by

print(increment(2, by=1)) # by=1 is our keword argument

# Default Arguments
# This arguments are called alongside the parameters so that incase they are not called in the function they will be returned by default
def incrementb(number, by=1):
    return number + by

print(incrementb(2))

# Printing multiple arguments but defining just one parameter
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total
print (multiply(2, 3, 4, 5))

# **args
# It enables us to pass multiple keyword arguments and python will pass them as a dictionary
def save_user(**user):
    print(user['name']) # we can get a specific value

save_user(id=1, name='John', age=22)