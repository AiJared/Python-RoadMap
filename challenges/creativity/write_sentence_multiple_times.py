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
    