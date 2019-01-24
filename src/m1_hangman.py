"""
Hangman.

Authors: Shixin Yan and Weizhou Liu.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. Implement Hangman using your Iterative Enhancement Plan.
####### Do NOT attempt this assignment before class! #######
import random

def main():
    setting_up_letter()
    get_a_random_letter_from_a_text_file()

def setting_up_letter():
    print('I will choose a random secret word from a dictionary. You set the MINIMUM length of that word.')
    MINIMUM_length = int(input('What MINIMUM length do you want for the secret word? '))
    print('It is your time to set the difficulty you want this game to have, with range from 0 to 10')
    HP = int(input('How many successful choioces do you want to allow yourself?'))
    return MINIMUM_length, HP

def get_a_random_letter_from_a_text_file():
    with open('words.txt') as f:
        f.readline()
        string = f.read()
    word = string.split()
    MINIMUM_length, HP = setting_up_letter()
    r = random.randrange(MINIMUM_length, len(word))
    item = word[r]









main()