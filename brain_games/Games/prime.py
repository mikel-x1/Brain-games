from sympy import isprime
import random


def rule():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime():
    question = random.randint(1, 100)

    if isprime(question):
        return int(question), 'yes'
    else:
        return int(question), 'no'
