import prompt


def start(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    ROUNDS = 3
    print(game.QUESTION)
    for _ in range(ROUNDS):
        answer, content = game.next_round()
        print(f'Question: {content}')
        ans = str(input('Your answer: '))
        if ans == str(answer):
            print('Correct!')
        else:
            print(f'{ans} is wrong answer ;(. \
Correct answer was {answer}.')
            print(f"Let's try again, {name}! ")
            break
        print(f'Congratulations, {name}!')
