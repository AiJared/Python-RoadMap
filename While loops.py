# While loop is a python feature that enables you to loop through a block of code if a certain condition is met
i = 1
while i < 6:
    print(i)
    i += 1

# 'Or' in a while loop
i = 1
while i < 6 or i == 6: # the code runs as long as one of the conditions is true
    print(i)
    i += 1

# 'And' in a while loop runs if all the conditions in the while loop are true
i = 1
while i < 6 and i == 6:
    print(i)
    i += 1 