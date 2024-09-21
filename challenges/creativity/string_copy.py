"""
Write a short Python function that takes a string s, representing a sentence,
and returns a copy of the string with all punctuation removed. 
For example, if given the string "Let s try, Mike.", this function would return
"Lets try Mike".
"""

def string_copy(string):
    punctuations = ["?", "!", ",", ".", "'"]
    result = ""
    # loop through each character in the string
    for char in string:
        # add character in result if it is not in punctuation
        if char not in punctuations:
            result += char
    return result

print(string_copy("Let's try, Mike."))