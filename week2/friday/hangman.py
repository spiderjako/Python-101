import sys
import os

def create_string(lst):
    st = ''.join(lst)
    return st

def anonymize(word):
    string_to_be_found = []
    for x in word:
        string_to_be_found.append('_ ')
    return string_to_be_found

def hangman(word):
    i = 0
    character = ''
    is_found = 1
    string_to_be_found = anonymize(word)

    while i < 10:
        character = input('Guess a letter: ')
        while len(character)!=1:
            character=input('It needs to be only 1 character, you dumbass! Guess a letter: ')
        
        if character in word:
            j = 0
            while j < len(word):
                if word[j].lower() == character or word[j].upper() == character :
                    string_to_be_found[j] = word[j]
                    string_to_be_found[j]+=' '
                j+=1
            print(create_string(string_to_be_found))
        else:
            print('Incorrect!')
            i+=1
        if '_ ' in string_to_be_found:
                    is_found=0
        if is_found == 1:
            print (create_string(string_to_be_found))
            print('Congratz')
            return
        is_found=1
    if i==10:
        print('You lost!')
    return

hang_word = sys.argv[1]
hangman(hang_word)
