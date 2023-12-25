import prompt


def start(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    ROUNDS = 3 
    print(game.QUESTION)
    while ROUNDS > 0:
        game.answer, game.content = game.round()
        print(game.content)
        ans = game.answer_type(input('Your answer: '))
        if ans == game.answer:
            ROUNDS -= 1
            print('Correct!')
        else:
            print(f'{ans} is wrong answer ;(. Correct answer was {game.answer}.')
            print(f"Let's try again, {name}! ")
            break
    if ROUNDS == 0:
        print(f'Congratulations, {name}!')