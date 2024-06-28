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

# Level 6: Variable Scope
global_var = 10

def some_function():
    local_var = 5
    print(global_var + local_var)

some_function()