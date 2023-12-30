from random import randint
import math


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_game_data():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    question = f'{number1} {number2}'
    answer = math.gcd(number1, number2)
    return str(answer), question
