#!/usr/bin/env python3

from brain_games.engine import game
from brain_games.games.calc import rule, calc


def main():
    game(rule, calc)


if __name__ == '__main__':
    main()
