#!/usr/bin/env python3

from brain_games.Engine import game
from brain_games.Games.progression import rule, progression


def main():
    print('Welcome to the Brain Games!')
    game(rule, progression)


if __name__ == '__main__':
    main()
    