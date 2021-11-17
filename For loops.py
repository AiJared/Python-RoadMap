# for loop is used for iterating over a sequence
# means that it used for looping over a sequence
for letter in 'Hello':
    print(letter)

# also works with any type
mylist = ['ji', 'ju', 'jo']

for values in mylist:
    print(values)

mydict = {
    'name': 'john',
    'age': 13,
}

for values in mydict:
    print(values)

# break stops the loop once the loops hits a certain value in the loop as shown by the if condition
mylist = ['ji', 'ju', 'jo']

for values in mylist:
    print(values)
    if values == 'ju':
        break

# putting a break befor the print function stops the loop at exactly the breaking value hence does not print that value
mylist = ['ji', 'ju', 'jo']

for values in mylist:
    if values == 'ju':
        break
    print(values)

# loop through a range of numbers
for x in range(4):
    print(x)

# loop through a particular range of numbers
for y in range(3, 7):
    print(y)

# for loop with else statement

for y in range(7):
    print(y) 
else:
    print('Finshed looping!!')   