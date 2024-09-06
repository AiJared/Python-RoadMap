def reverse_list(n):
    result_list = []
    
    # loop through the list from the end to the first one
    for i in range(len(n)-1,-1,-1):
        result_list.append(n[i])
    
    return result_list

print(reverse_list([3,5,6,4,2]))

# Using slicing

def reverse_list(n):
    return n[::-1]

print(reverse_list([3,5,6,4,2]))
