# Functions is a bunch of code which perform a particular task
# It uses a key word 'def' followed by the function and parenthesis
# The next line is indented
# An indent is equal to four spaces
# Passing a parameter in a function
def greetings_function(name):
    print('Welcome '+name)

greetings_function('John') 

# Passing more than one parameter

def greetings_functionA(name, age):
    print('Welcome '+name+'. You are '+str(age)+ ' years old')

greetings_functionA('John', 27)

# Function with many values that returns a specific value i.e. greet a specif name from our example
def greetings_functionB(*names):
    print('Welcome '+names[1])

greetings_functionB('John', 'Tim', 'Tom')

# Another way of passing name and age
def greetings_functionC(name, age):
    print('Welcome '+name+'. You are '+str(age)+ ' years old')

greetings_functionC(name = 'John', age = 27)

# Ask the user to put values using the input function
def greetings_functionD(name, age):
    print('Welcome '+name+'. You are '+str(age)+ ' years old')

name = input('Enter your name: ')
age = input('Enter your age: ')
greetings_functionD(name, age)