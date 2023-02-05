import prompt
import random


def game():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        number = random.randint(0, 100)
        print(f'Question: {number}')
        answer = prompt.string()
        print(f'Your answer: {answer}')
        if number % 2 == 0:
            if answer == 'yes':
                print('Correct!')
                i += 1
            else:
                print("'yes' is wrong answer ;(. Correct answer was 'no'.")
                i = 0
        else:
            if answer == 'no':
                print('Correct!')
                i += 1
            else:
                print("'no' is wrong answer ;(. Correct answer was 'yes'.")
                i = 0
    print(f'Congratulations, {name}!')
