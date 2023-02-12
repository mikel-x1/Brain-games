#!/usr/bin/env python3

from brain_games.engine import game
from brain_games.games.prime import rule, prime


def main():
    game(rule, prime)


if __name__ == '__main__':
    main()
