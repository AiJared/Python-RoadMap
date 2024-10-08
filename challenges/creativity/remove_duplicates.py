# Task
"""
Write the Python function that takes a list as input then removes duplicates keeping the order
of first occurrence of each element.
"""
# Steps
"""
- You can use a loop to iterate through the list as you add elements into a new list if they aren't
added already.
- You a helper structure like set to track elements that have been added to the new list.
"""

def remove_duplicates(lst):
    unique_elements = [] # Create an empty list that will be used to store the unique elemets
    seen = set() # Create a set that will be used to track elements that have already been added to the new list

    for num in lst: # Iterate over each element of the original list
        if num not in seen: # Check if an element has not yet been tracked by the set
            unique_elements.append(num) # Append elements not yet seen to the unique elements list
            seen.add(num) # Once an element has been added to unique elements, add it to seen as well
    
    # Output the new list of unique elements
    return unique_elements

print(remove_duplicates([1,2,2,3,4,4,5]))

# Second Approach
"""
This approach works by converting the original list into a set so that duplicates can be
discarded then convert that set into a list again.
However, it does not guarantee maiting the order of the list but it surely removes the duplicates.
So if maintaining order matters, then the first approach is the most appropriate but if
it doesn't then both approaches are better with the second approach even being much simpler to
implement.
"""

def rm_duplicates(lst):
    new_list = list(set(lst))
    return new_list

print(rm_duplicates([1,2,2,3,4,4,5]))