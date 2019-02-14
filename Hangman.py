#!/usr/bin/python3


import time
import random
import os
import sys


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def printhangman(lifepoint):
    with open("hangart.txt", "r") as f:
        hangman = f.readlines()
        hangmanpic = [
                hangman[111:135], hangman[85:109], hangman[59:83], hangman[33:57],
                hangman[9:31], hangman[1:7], ' '
                ]
        for line in hangmanpic[lifepoint]:
            print(line, end="")
    f.close()


def menu():
    start = 0
    with open('title.txt', 'r') as title:
        text = title.readlines()
        for line in text:
            print(line, end="")
    user_input = input()
    if user_input == '1':
        start = 1

    elif user_input == '2':
        start = 2

    elif user_input == '3':
        start = 3
        sys.exit()
    return start


def import_file(country, capitals):
    with open('capitals.txt', 'r') as temp:
        for line in temp:
            (key, value) = line.split(' | ')
            value = str(value[:-1])
            country.append(key)
            capitals.append(value)
        return country, capitals


def generator(hint, country, capitals):
    pick = random.randint(0, 182)
    hint.append(country[pick])
    picked = capitals[pick]
    return picked


def play(picked, blank, answer):
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


def player_move(lifepoint, answer, blank, used_letter):
    
    position=[]            
    user_input = input()
    user_input2 = user_input.upper()
    user_input3 = user_input.lower()
    if user_input in answer or user_input2 in answer or user_input3 in answer:
        for i, letter in enumerate(answer):
            if user_input.casefold() == letter.casefold():
                position.append(i)
                print(position)
                for pos in position:
                    blank[pos] = ' '+letter.upper()+' '
    else:
        lifepoint = lifepoint - 1
        used_letter.append(user_input)        
    return lifepoint


def score(name_score, game_time, lifepoint):

    name = input('Enter your name: ')
    name_score[name] = game_time
    if lifepoint > 0:
        with open('score.txt', 'a') as temp:
            temp.write('{:s} {:d}'.format(name, game_time))
            temp.write('\n')
            temp.close()


def display_score():
        cls()
        temp_dict = {}
        with open('score.txt', 'r') as temp:
            for line in temp:
                (key, value) = line.split(' ')
                value = value[:-1]
                value = int(value)
                temp_dict[key] = value
        sorted_values = sorted(temp_dict.values())
        counter = 1
        for list_values in sorted_values:
            for name, score in temp_dict.items():
                if list_values == score:
                    print(str(counter) + ': ' + str(name) + ' | '+str(score))
            counter += 1
        p1 = input('Press any key to return to menu')


def result(elapsed_time, name_score, lifepoint):
    while_start = True
    print('Game time: ' + str(elapsed_time) + ' seconds')
    score(name_score, elapsed_time, lifepoint)
    p_input = input('Do you want to play again? (y/n)')
    if p_input == 'y' or p_input == 'Y':
        while_start = False
    elif p_input == 'n' or p_input == 'N':
        cls()
        exit()

    return while_start


def win_lose(lifepoint, hint, blank, used_letter, elapsed_time, name_score, game_time):
    game_time = elapsed_time
    while_start = True
    space = ' _ '
    if lifepoint <= 2:
        print('The capital of: '+str(hint[0]))

    if lifepoint == 0:
        cls()
        printhangman(lifepoint)
        print('You lost!')
        while_start = result(elapsed_time, name_score, lifepoint)

    elif space not in blank:
        cls()
        print_out(blank, used_letter, lifepoint)
        print('You win')
        while_start = result(elapsed_time, name_score, lifepoint)

    return while_start


def print_out(blank, used_letter, lifepoint):
    counter = 0
    for _ in blank:
        print(blank[counter], end='')
        counter = counter + 1
    print('\n')
    print('Lifepoints: '+str(lifepoint))
    print('\n')
    if len(used_letter) > 0:
        print('Used letters not in the word: ')
        for notletter in range(len(used_letter)):
            print(used_letter[notletter].upper(), end=', ')
    print('\n')


def main():
    while True:
        cls()
        game_time = 0
        elapsed_time = 0
        start = 0
        start = menu()
        if start == 1:
            name_score = {}
            lifepoint = 6
            country = []
            capitals = []
            answer = []
            blank = []
            hint = []
            used_letter = []
            import_file(country, capitals)
            picked = generator(hint, country, capitals)
            play(picked, blank, answer)
            start_time = time.time()
            while win_lose(lifepoint, hint, blank, used_letter, elapsed_time, name_score, game_time):
                cls()
                print_out(blank, used_letter, lifepoint)
                win_lose(lifepoint, hint, blank, used_letter, elapsed_time, name_score, game_time)
                printhangman(lifepoint)
                lifepoint = player_move(lifepoint, answer, blank, used_letter)
                end_time = time.time()
                elapsed_time = int(end_time - start_time)
        elif start == 2:
            display_score()
            '''cls()
            pos = 1
            with open('score.txt', 'r') as temp:
                for line in temp:
                    print(str(pos)+': '+line)
                    pos += 1
            p1 = input('Press enter to return menu!')'''

if  __name__ == "__main__":
    
    main()