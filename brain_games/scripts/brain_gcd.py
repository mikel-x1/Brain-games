#!/usr/bin/env python3

from brain_games.Engine import game
from brain_games.Games.gcd import rule, gcd


def main():
    print('Welcome to the Brain Games!')
    game(rule, gcd)


if __name__ == '__main__':
    main()
