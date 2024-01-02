from random import randint
from math import sqrt


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False


def generate_game_data():
    asked_number = randint(1, 100)
    question = asked_number
    answer = 'yes' if is_prime(asked_number) else 'no'
    return answer, question
