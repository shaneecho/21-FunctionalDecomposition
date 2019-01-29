"""
Hangman.

Authors: Shixin Yan and Weizhou Liu.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. Implement Hangman using your Iterative Enhancement Plan.
####### Do NOT attempt this assignment before class! #######
import random

def main():
    print('I will choose a random secret word from a dictionary. You set the MINIMUM length of that word.')
    MINIMUM_length = int(input('What MINIMUM length do you want for the secret word? '))
    print('It is your time to set the difficulty you want this game to have, with range from 0 to 10')
    HP = int(input('How many successful choioces do you want to allow yourself?'))
    get_a_random_letter_from_a_text_file(MINIMUM_length)
    letter = input('What letter do you want to try?')
    check_letter(letter,HP,MINIMUM_length)

def get_a_random_letter_from_a_text_file(MINIMUM_length):
    with open('words.txt') as f:
        f.readline()
        string = f.read()
    word = string.split()
    while True:
        r = random.randrange(0, len(word))
        item = word[r]
        if len(item)>=MINIMUM_length:
            break
    ret = ''
    for k in range(len(item)):
        ret = ret + '- '
    print(ret)
    return item,ret

def check_letter(letter,HP,MINIMUM_length):
    item,ret = get_a_random_letter_from_a_text_file(MINIMUM_length)
    for k in range()






main()