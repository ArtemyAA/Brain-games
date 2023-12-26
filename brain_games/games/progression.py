#!/usr/bin/env python3

from random import randint
from random import choice

answer_type = int
QUESTION = 'What number is missing in the progression?'


def round():
    start_number = randint(1, 10)
    step = randint(1, 10)
    progression = list(range(start_number, start_number + 10 * step, step))
    index = len(progression) - 1
    random_index = choice(range(0, index))
    answer = progression[random_index]
    content = ''
    for i in progression:
        if i == answer:
            content += ".. "
        else:
            content += f'{str(i)} '
    return answer, content
