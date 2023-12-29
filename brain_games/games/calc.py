from random import randint
from random import choice


DISCRIPTION = 'What is the result of the expression?'


def generate():
    number1 = randint(1, 20)
    number2 = randint(1, 20)
    operator = choice('-+*')
    if operator == '+':
        answer = number1 + number2
    elif operator == '-':
        answer = number1 - number2
    elif operator == '*':
        answer = number1 * number2
    question = f'{number1} {operator} {number2}'
    return answer, question
