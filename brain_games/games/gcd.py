#!/usr/bin/env python3

from random import randint
import math


QUESTION = 'Find the greatest common divisor of given numbers.'


def next_round():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    content = f'{number1} {number2}'
    answer = math.gcd(number1, number2)
    return answer, content
