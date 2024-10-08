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
    unique_elements = []
    seen = set()

    for num in lst:
        if num not in seen:
            unique_elements.append(num)
            seen.add(num)
    
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