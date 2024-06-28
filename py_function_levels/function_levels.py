# Level 1: Basic Function
def my_function():
    print("Hello, world!")

# Level 2: Function with Parameters
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# Level 3: Return Values
def add(a, b):
    return a + b

result = add(2, 3)
print(result)

# Level 4: Default Parameters
def greet(name="Guest"):
    print(f"Hello, {name}")

greet()

# Level 5: Docstrings
def add(a, b):
    """
    This function adds two numbers
    """
    return a + b

result = add(2, 3)
print(result)

# Level 6: Variable Scope
global_var = 10

def some_function():
    local_var = 5
    print(global_var + local_var)

some_function()

# Level 7: Recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
result = factorial(8)
print(result)

# Level 8: Lambda Functions
double = lambda x: x * 2
result = double(3)
print(result)

# Level 9: Function Decorators
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# Level 10: Advanced Functions
def apply(func, x):
    return func(x)

def square(x):
    return x ** 2

result = apply(square, 5)
print(result)