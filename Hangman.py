#!/usr/bin/python3

import time
import random, os, sys
lifepoint = 1

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
    
    position=[]            
    user_input = input()
    user_input2 = user_input.upper()
    user_input3 = user_input.lower()
    if user_input in answer or user_input2 in answer or user_input3 in answer:
        for letter in answer:
            if user_input == letter or user_input2 == letter or user_input3 == letter:
                for i in range(len(answer)):
                    if letter == answer[i]:
                        position.append(i)
                        print(position)
                        for pos in position:
                            blank[pos] = ' '+letter.upper()+' '
                    else:
                       pass
    else:
        lifepoint = lifepoint - 1            
    return lifepoint            

def score(name_score):


    name = input('Enter your name: ')
    name_score[name] = 0
    with open('score.txt', 'a') as temp:
        temp.write(name)
        temp.write('\n')
        temp.close()


def win_lose(lifepoint):

    torf = True
    space = ' _ '
    if lifepoint <=2:
        print('The capital of: '+str(hint[0]))

    if lifepoint == 0:
        cls()
        printhangman(lifepoint)
        print('You lost!')
        print('Game time: ' +str(elapsed_time) + ' seconds' )
        p_input = input('Do you want to play again? (y/n)')
        if p_input == 'y' or p_input == 'Y':
            start = 0
            torf = False
        elif p_input == 'n' or p_input == 'N':
            cls()
            exit()

    elif space not in blank:
        cls()
        print_out()
        print ('You win')
        print('Game time: ' +str(elapsed_time) + ' seconds' )
        p_input = input('Do you want to play again? (y/n)')
        if p_input == 'y' or p_input == 'Y':
            start = 0
            torf = False
        elif p_input == 'n' or p_input == 'N':
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
    if start == 1:
        name_score = {}
        score(name_score)
        lifepoint = 6
        country =[]
        capitals=[]
        answer = []
        blank = []
        hint = []
        import_file()
        picked = generator()
        start_time = time.time()
        play()
        while win_lose(lifepoint):
            cls()
            print_out()
            win_lose(lifepoint)
            printhangman(lifepoint) 
            lifepoint=p_move(lifepoint)
            end_time = time.time()
            elapsed_time = int(end_time - start_time)


