#!/usr/bin/env python3

from random import randint
from random import choice

QUESTION = 'What is the result of the expression?'
answer_type = int

def round():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    operator = choice('-+*')
    if operator == '+':
        answer = number1 + number2
    elif operator == '-':
        answer = number1 - number2
    elif operator == '*':
        answer = number1 * number2
    content = f'{number1}{operator}{number2}' 
    return answer, content
        