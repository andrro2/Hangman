from random import randint
import sys

capitals = ['SOFIA', 'PARIS', 'HELSINKI', 'BERLIN', 'ATHENS', 'BUDAPEST']

def menu():
    start = 0
    print('Welcome to Hangman game!' '\n' 'Start (1)' '\n' 'Scores(2)' '\n' 'Exit(3)')
    user_input = input()
    if user_input == '1':
        start = 1
        return start

    elif user_input == '2':
        start = 2
        return start
        pass

    elif user_input == '3':
        start = 3
        return start



