#!/usr/bin/python3

import time
import random
country =[]
capitals=[]

def printhangman(lifepoint):
    with open("hangart.txt", "r") as f:
        hangman = f.readlines()
        hangmanpic = [hangman[111:135],hangman[85:109],hangman[59:83],hangman[33:57],hangman[9:31],hangman[1:7]]
        for line in hangmanpic[lifepoint]:
            print(line, end="")
    f.close()

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

    elif user_input == '3':
        start = 3
        return start

def win():



def play(letter):
    for letter in picked():
        print('_' * len(picked))


# Start = time.time()
# time.process_time()
# End = time.time()

def import_file():
    temp = open('capitals.txt', 'r')
    for line in temp:
            (key, value) = line.split(' | ')
            value = str(value[:-1])
            country.append(key)
            capitals.append(value)
    return country, capitals


def generator():
    pick = random.randint(0, 182)
    picked = capitals[pick]
    return picked


import_file()
picked = generator()
