import prompt
import random


def rule():
    return 'What is the result of the expression?'


def calc():
    number_1 = random.randint(10, 100)
    number_2 = random.randint(1, number_1)
    k = random.random()
    if k < 0.5:
        return f'{number_1} + {number_2}', str(number_1 + number_2)
    else:
        return f'{number_1} - {number_2}', str(number_1 - number_2)

