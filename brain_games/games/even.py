from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_game_data():
    asked_number = randint(1, 100)
    question = asked_number
    if asked_number % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return answer, question
