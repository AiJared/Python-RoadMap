"""
Write a short Python function that counts the number of vowels in a given
character string.
"""
def count_vowels(character_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in character_string.lower():
        if char in vowels:
            count += 1
    return count

print(count_vowels("Jared"))