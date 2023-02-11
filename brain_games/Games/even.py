import random


def rule():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def even():
    number = random.randint(0, 100)
    if number % 2 == 0:
        return number, 'yes'
    else:
        return number, 'no'
