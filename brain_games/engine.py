import prompt


ROUNDS = 3


def start(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.DISCRIPTION)
    for _ in range(ROUNDS):
        right_answer, question = game.generate()
        print(f'Question: {question}')
        user_answer = str(input('Your answer: '))
        if user_answer == str(right_answer):
            print('Correct!')
            continue
        else:
            print(f'{user_answer} is wrong answer ;(. \
Correct answer was {right_answer}.')
            print(f"Let's try again, {name}! ")
            break
    else:
        print(f'Congratulations, {name}!')
# исправил for/else и логику. правильно ли здесь написан код и в целом for/else?
