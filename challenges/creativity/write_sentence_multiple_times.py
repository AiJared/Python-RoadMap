"""
A common punishment for school children is to write out a sentence multiple times. 
Write a Python stand-alone program that will write out the
following sentence one hundred times: “I will never spam my friends
again.” Your program should number each of the sentences and it should
make eight different random-looking typos.
"""
import random

def introduce_typo(sentence):
    # choose a random position in the sentence to introduce a typo
    typo_index = random.randint(0, len(sentence) - 1)
    # choose a random character to replace the character at typo index
    random_char = chr(random.randint(97, 122)) # random lowercase letter

    # create a typo by replacing the character at typo index
    typo_sentence = sentence[:typo_index] + random_char + sentence[typo_index + 1:]

    return typo_sentence

def write_with_typos():
    sentence = "I will never spam my friends again."
    typo_count = 8
    typo_positions = random.sample(range(1, 101), typo_count) # 8 unique positions out of 100

    for i in range(1, 100):
        if i in typo_positions:
            # introduce a typo in the sentence
            output_sentence = introduce_typo(sentence)
        else:
            # no typo, use the correct sentence
            output_sentence = sentence