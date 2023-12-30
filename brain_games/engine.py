import prompt


ATTEMPTS = 3  # дал более точное именование константы и расположил под импортом


def start_game(game_name):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game_name.DESCRIPTION)
    for _ in range(ATTEMPTS):
        right_answer, question = game_name.generate_game_data()
        print(f'Question: {question}')
        user_answer = input('Your answer: ')
        if user_answer == right_answer:
            print('Correct!')
        else:
            print(f'{user_answer} is wrong answer ;(. \
Correct answer was {right_answer}.')
            print(f"Let's try again, {user_name}! ")
            break
    else:
        print(f'Congratulations, {user_name}!')
# в целом прошелся по именованию и всем переменным дал более точное названия
