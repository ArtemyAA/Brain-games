#!/usr/bin/env python3

from random import randint


QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def next_round():
    asked_number = randint(1, 100)
    content = asked_number
    div_amount = 0
    for i in range(1, asked_number + 1):
        if asked_number % i == 0:
            div_amount += 1
    if div_amount == 2:
        answer = 'yes'
    else:
        answer = 'no'
    return answer, content
