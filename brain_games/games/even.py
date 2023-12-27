#!/usr/bin/env python3

from random import randint


QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def next_round():
    asked_number = randint(1, 100)
    content = asked_number
    if asked_number % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return answer, content
