#!/usr/bin/env python3

from brain_games.scripts.brain_games import main
import prompt
from random import randint

def even_game():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 3
    name = welcome_user()
    while count != 0:
        asked_number = randint(1, 100)
        answer = prompt.string(f'Question: {asked_number}\nYour answer: ')
        check = bool(asked_number % 2 == 0) #True or False
        if check == True and answer == 'yes' or check == False and answer == 'no':
            count -= 1
            print('Correct!')
        else:
            print('"yes" is wrong answer ;(. Correct answer was "no".')
            print(f"Let's try again, {name}! ")
            break
    if count == 0:
        print(f'Congratulations, {name}')

if __name__ == '__main__':
    main()
    even_game()
        
