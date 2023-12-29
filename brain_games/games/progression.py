from random import randint
from random import choice


DISCRIPTION = 'What number is missing in the progression?'


def generate():
    start_number = randint(1, 10)
    step = randint(1, 10)
    progression = list(range(start_number, start_number + 10 * step, step))
    random_index = choice(range(0, len(progression) - 1))
    answer = progression[random_index]
    progression[random_index] = '..'
    question = ' '.join(map(str, progression))
    return answer, question
