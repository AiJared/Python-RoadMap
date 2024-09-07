"""
Write a short Python function that takes a sequence of integer values and
determines if there is a distinct pair of numbers in the sequence whose
product is odd.
"""
def distinct_odd_pair(nums):
    distinct_pairs = []

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            # check if both numbers are odd
            if nums[i] % 2 != 0 and nums[j] % 2 != 0:
                distinct_pairs.append((nums[i], nums[j]))
    
    return distinct_pairs

print(distinct_odd_pair([1,2,3,4,5,6,7,9]))