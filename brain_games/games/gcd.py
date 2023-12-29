from random import randint
import math


DISCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    question = f'{number1} {number2}'
    answer = math.gcd(number1, number2)
    return answer, question
