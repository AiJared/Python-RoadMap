# If statement is basically giving python a condition
# It allows python to execute code automatically by itself as long as the condtion is true
a = 4
b = 3
if a>b:
    print(str(a) + ' is greater than ' + str(b))

# Can also work with different data types
a = 'Tim'
b = 'Tim'

if a == b:
    print('a is equal to b')

a = True
b = 'Tim'

if a == True:
    print('a is True')

a = False
b = 'Tim'

if a  != True:
    print('a is not True')

a = 4
b = 3

if a >= b:
    print('True')

# else statement returns otherwise if the condition is not True
a = 4
b = 5

if a == b:
    print('A equals B')
else:
    print('A not equals B')

# if else statement can also be used with other data types
a = False
b = 5

if a == True:
    print('A is true')
else:
    print('A not true')

# if else statement can work with more than one condition with an 'elif' statement
a = False
b = 5

if a == True:
    print('A is true')
elif a == False:
    print('A is false')
else:
    print('A is none of the above')

# if statements with 'or' & 'and'
# with 'or' the only the first condition is checked
boy = True
short = True

if boy == True or short == False:
    print('He is a boy or he is short')

# with 'and' both conditions must be met for the code to execute
boy = True
short = True

if boy == True and short == False:
    print('He is a boy or he is short') # for this case it returns nothing because one of the conditons is not met
  # 'or' and 'and' with an else statement
else:
    print('He is a boy but not short.')

# using input method and also check for a specific data type
value = input('Input a value: ')

if type(value) == str:
    print(value+ ' is a string')
else:
    print(value+ ' is not a string')

value = int(input('Input a value '))

if type(value) == str:
    print(value+ ' is a string')
else:
    print(value, ' is not a string')

# check if a number is divisible by 5
value = int(input('Input a number: '))

if value%5 == 0:
    print(value, 'can be divided by 5')
else:
    print(value, 'cannot be divided by 5')