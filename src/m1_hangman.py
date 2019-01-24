"""
Hangman.

Authors: Shixin Yan and Weizhou Liu.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. Implement Hangman using your Iterative Enhancement Plan.
####### Do NOT attempt this assignment before class! #######
import random

def main():
    check_letter()

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
    MINIMUM_length,HP= setting_up_letter()
    while True:
        r = random.randrange(0, len(word))
        item = word[r]
        if len(item)>=MINIMUM_length:
            break
    ret = ''
    for k in range(len(item)):
        ret = ret + '- '
    print('Here is what you currently know about the secret word:')
    print(ret)
    return item

def receive_letter_from_user():
    letter=input('What letter do you want to try?')
    return letter

def check_letter():
    item=get_a_random_letter_from_a_text_file()
    letter=receive_letter_from_user()
    for k in range(len(item)):
        if item[k]==letter:












main()