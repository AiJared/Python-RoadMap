# 2D lists is a list that contains a list
my_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(my_list)

#get the value of the first value of the first inner list
print(my_list[0][0])

# Nested loop is a loop that is inside a loop
my_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for lists in my_list:
    for row in lists:
        print(row)