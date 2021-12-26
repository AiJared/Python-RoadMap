def my_function(country = 'Norway'): # country is a parameter and Norway is a default argument
    print('I am from '+ country)
my_function('Kenya') # Kenya is arguments
my_function()# It will return the default argument specified in the parameter above
my_function('USA')
my_function('Great Britain')

def my_func(x):
    return 5 * x
print(my_func(2))
print(my_func(3))
print(my_func(4))

# Recursion
def try_recursion(k):
    if (k>0):
        result = k + try_recursion(k-1)
        print(result)
    else:
        result = 0
    return result
    print("\n\nRecursion Example Results")
try_recursion(6)

# lambda function
# lambda is a small anonimous function that takes many arguments but in the end only have one expression
x = lambda a: a + 10
print(x(5))

b = lambda k: k * 20
print(b(10))

i = lambda j, n: j * n
print(i(10, 20))

# lamda function inside another function
def func(n):
    return lambda a: a * n
mydoubler = func(2)
mytrippler = func(3)
print(mydoubler(11))
print(mytrippler(11))