from random import randint

capitals = ['Sofia', 'Paris', 'Helsinki', 'Berlin', 'Athens', 'Budapest']

def menu():
    start = 0
    print('Welcome to Hangman game!' '\n' 'Start (1)' '\n' 'Exit(4)')
    user_input = input()
    if user_input == '1':
        start = 1
        return start
    elif user_input == '4':
        start = 4
        return start


