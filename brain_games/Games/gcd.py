import prompt
import random
import math


def rule():
    return 'Find the greatest common divisor of given numbers.'


def gcd():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    return f'{number_1} {number_2}', str(math.gcd(number_1, number_2))
