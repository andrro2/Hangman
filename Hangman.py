#!/usr/bin/python3

import time
import random, os, sys
lifepoint = 6

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def printhangman(lifepoint):
    with open("hangart.txt", "r") as f:
        hangman = f.readlines()
        hangmanpic = [hangman[111:135],hangman[85:109],hangman[59:83],hangman[33:57],hangman[9:31],hangman[1:7], ' ']
        for line in hangmanpic[lifepoint]:
            print(line, end="")
    f.close()

def menu():
    start = 0
    with open('title.txt', 'r') as title:
        text = title.readlines()
        for line in text:
            print(line,end="")
    user_input = input()
    if user_input == '1':
        start = 1

    elif user_input == '2':
        start = 2

    elif user_input == '3':
        start = 3
        sys.exit()
    return start

def import_file():
    with open('capitals.txt', 'r') as temp:
        for line in temp:
            (key, value) = line.split(' | ')
            value = str(value[:-1])
            country.append(key)
            capitals.append(value)
        return country, capitals


def generator():
    pick = random.randint(0, 182)
    hint.append(country[pick])
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
    lifeloss = 0
    position=[]            
    user_input = input()
    user_input2 = user_input.upper() 
    if user_input in answer or user_input2 in answer:
        for letter in answer:
            if user_input == letter or user_input2 == letter:
                for i in range(len(answer)):
                    if letter == answer[i]:
                        position.append(i)
                        print(position)
                        for pos in position:
                            blank[pos] = ' '+letter.upper()+' '
                        lifeloss = 0
                    else:
                       lifeloss = 0
    else:
        lifepoint = lifepoint - 1            
    return lifepoint            

        

def win_lose(lifepoint):
    torf = True
    space = ' _ '
    if lifepoint <=2:
        print('The capital of: '+str(hint[0]))

    if lifepoint == 0:
        cls()
        print('You lost!')
        printhangman(lifepoint)
        p_input = input('Do you want to play again? (y/n)')
        if p_input == 'y':
            start = 0
            torf = False
        elif p_input == 'n':
            cls()
            exit()

    elif space not in blank:
        cls()
        print_out()
        print ('You win')
        p_input = input('Do you want to play again? (y/n)')
        if p_input == 'y':
            start = 0
            torf = False
        elif p_input == 'n':
            cls()
            exit()
    return torf


def print_out():
    counter = 0
    for i in blank:
        print(blank[counter], end='')
        counter = counter + 1

    print ('\n')
    print('Lifepoints: '+str(lifepoint))
    print ('\n')


while True:
    cls()
    start = 0
    start=menu()
    lifepoint = 6
    if start == 1:
        country =[]
        capitals=[]
        answer = []
        blank = []
        hint = []
        import_file()
        picked = generator()
        play()
        while win_lose(lifepoint):
            cls()
            print_out()
            win_lose(lifepoint)
            printhangman(lifepoint) 
            lifepoint=p_move(lifepoint)



