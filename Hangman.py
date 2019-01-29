from random import randint
import sys


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



def import_file():
    capitals = {}
    temp = open('capitals.txt', 'r')
    for line in temp:
            (country, capital) = line.split(' | ')
            capital = str(capital[:-2])
            capitals[country] = capital
    return capitals

capitals = import_file()
print(capitals)