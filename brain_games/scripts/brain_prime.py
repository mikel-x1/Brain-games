#!/usr/bin/env python3

from brain_games.Engine import game
from brain_games.Games.prime import rule, prime


def main():
    print('Welcome to the Brain Games!')
    game(rule, prime)


if __name__ == '__main__':
    main()
