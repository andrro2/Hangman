#!/usr/bin/python3

import time
import random, os, sys
country =[]
capitals=[]
answer = []
blank = []
lifepoint = 6

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def printhangman(lifepoint):
    with open("hangart.txt", "r") as f:
        hangman = f.readlines()
        hangmanpic = [hangman[111:135],hangman[85:109],hangman[59:83],hangman[33:57],hangman[9:31],hangman[1:7]]
        for line in hangmanpic[lifepoint]:
            print(line, end="")
    f.close()

def menu():
    start = 0
    user_input = input('Welcome to Hangman game!' '\n' 'Start (1)' '\n' 'Scores(2)' '\n' 'Exit(3)' '\n')
    if user_input == '1':
        start = 1

    elif user_input == '2':
        start = 2

    elif user_input == '3':
        start = 3
        sys.exit()
    return start

#Start = time.time()
#time.process_time()
#End = time.time()

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


def play():
    counter = 0
    for letters in picked:
        blank.append(' _ ')
        answer.append(letters)
    for space in answer:
        if space == ' ':
            blank[counter] = '   ' 
            counter = counter + 1
        else:
            counter = counter+1
            pass
def p_move():            
    user_input = input()
    user_input = str(user_input.upper) 
    if user_input in answer:
        counter = 0
        for letter in answer:
            if user_input == letter:
                    blank[counter] = letter
            else:
                    life -= 1

    else:
        life -= 1

cls()
menu()

