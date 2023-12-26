#!/usr/bin/env python3

from random import randint
from random import choice

answer_type = int
QUESTION = 'What is the result of the expression?'


def round():
    number1 = randint(1, 20)
    number2 = randint(1, 20)
    operator = choice('-+*')
    if operator == '+':
        answer = number1 + number2
    elif operator == '-':
        answer = number1 - number2
    elif operator == '*':
        answer = number1 * number2
    content = f'{number1} {operator} {number2}'
    return answer, content
