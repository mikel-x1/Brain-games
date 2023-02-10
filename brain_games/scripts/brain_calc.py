#!/usr/bin/env python3

from brain_games.Engine import game
from brain_games.Games.calc import rule, calc


def main():
    print('Welcome to the Brain Games!')
    game(rule, calc)


if __name__ == '__main__':
    main()