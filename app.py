# Print function
print('Hello world, my name is Jared, my age is',100)
print('welcome')

#Varaibles in python
name = 'Tim'
print('Tim is a boy')
print('Tim is 18')
print('Tim is from Turkey')
print(name)

# Concatnation is joining the varaible and the normal string together
# We can use + with a string and we can use , with a string and an integer.
age = 18
print(name+' is a boy')
print(name,'is', age)
print(name+' is from Turkey')
print(name)

# printing a string on two different lines without adding another print function
print('Hi.\nHow are you')

# To print special characters we use a backslash
print('Hi\'How are you')

# To print different letters on a python string
print(name[0])

# Change a string into upper and lowercases
print(name.upper())
print(name.lower())

# Check whether a string is in upper or lowercase
print(name.islower())

#convert a string to lower and check
print(name.lower().islower())

#Print the number of characters that a string has
print(len(name))

# Print the index number of a character
print(name.index('i'))

#Replace text with another one
print(name.replace('m', 't'))