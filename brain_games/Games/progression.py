import random


def rule():
    return 'What number is missing in the progression?'


def progression():
    a = random.randint(1, 20)
    d = random.randint(1, 10)
    b = a + 10 * d
    prog = list(range(a, b + 1, d))
    i = random.randint(0, 10)
    answer = prog[i]
    for k in range(len(prog)):
        prog[k] = str(prog[k])
    prog[i] = '..'
    question = ' '.join(prog)
    return question, str(answer)
