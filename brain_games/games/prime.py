from random import randint


DISCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    div_amount = 0
    for i in range(1, number + 1):
        if number % i == 0:
            div_amount += 1
    return True if div_amount == 2 else False


def generate():
    asked_number = randint(1, 100)
    question = asked_number
    answer = 'yes' if is_prime(asked_number) else 'no'
    return answer, question
