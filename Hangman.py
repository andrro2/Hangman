#!/usr/bin/python3

import time
import random, os, sys
lifepoint = 1

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
    user_input3 = user_input.lower()
    if user_input in answer or user_input2 in answer or user_input3 in answer:
        for letter in answer:
            if user_input == letter or user_input2 == letter or user_input3 == letter:
                for i in range(len(answer)):
                    if letter == answer[i]:
                        position.append(i)
                        print(position)
                        for pos in position:
                            blank[pos] = ' '+letter+' '
                        lifeloss = 0
                    else:
                       lifeloss = 0
    else:
        lifepoint = lifepoint - 1            
    return lifepoint            

        

def win_lose(lifepoint):
    space = ' _ '
    
    if lifepoint == 0:
        print('You lost!')
        return False

    elif space not in blank:
        print ('You win!')
    return True
    
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
    start=menu()
    if start == 1:
        country =[]
        capitals=[]
        answer = []
        blank = []
        import_file()
        picked = generator()
        start_time = time.time()
        play()
        if lifepoint == 0:
            lifepoint += 6
        while win_lose(lifepoint):
            cls()
            print_out()
            printhangman()
            print(answer)
            end_time = time.time()
            elapsed_time = end_time - start_time
            print('Elapsed time: ''%dseconds' %(elapsed_time))
            lifepoint=p_move(lifepoint)


