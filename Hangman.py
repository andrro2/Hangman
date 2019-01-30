#!/usr/bin/python3

import time
import random, os, sys
lifepoint = 6

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def printhangman():
    with open("hangart.txt", "r") as f:
        hangman = f.readlines()
        hangmanpic = [hangman[111:135],hangman[85:109],hangman[59:83],hangman[33:57],hangman[9:31],hangman[1:7], ' ']
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

def p_move(lifepoint):            
    user_input = input()
    user_input2 = user_input.upper() 
    if user_input in answer or user_input2 in answer:
        for letter in answer:
            if user_input == letter or user_input2 == letter:
                    blank[letter] = letter
            else:
                    lifepoint = lifepoint - 1


    else:
        lifepoint = lifepoint - 1

def win_lose():
    space = ' _ '
    if space not in blank:
        print ('You win')

    elif lifepoint == 0:
        print('You lost!')

def print_out():
    counter = 0
    for i in blank:
        print(blank[counter], end='')
        counter = counter + 1

    print ('\n')
    print(lifepoint)
    print ('\n')

cls()
start=menu()
while True:
    if start == 1:
        country =[]
        capitals=[]
        answer = []
        blank = []
        lifepoint = 6
        import_file()
        picked = generator()
        play()
        while True:
            printhangman()
            print_out()
            p_move(lifepoint)
            win_lose()
            print(answer)
            print(blank)
            print(lifepoint)




