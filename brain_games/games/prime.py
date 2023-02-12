import random


def rule():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def isprime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n


def prime():
    question = random.randint(1, 100)

    if isprime(question):
        return question, 'yes'
    else:
        return question, 'no'
