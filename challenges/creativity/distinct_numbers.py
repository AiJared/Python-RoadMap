"""
Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are distinct).
"""

"""
The simplest way of doing this is by comparing the length of the list and the length of the set
created from that list. Since set cannot contain duplicate values, if the lengths are the same
then the numbers are different.
"""

def distinct_nums(nums):
    return len(nums) ==  len(set(nums))

print(distinct_nums([2,3,4,5]))
print(distinct_nums([2,2,3,4]))