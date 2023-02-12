#!/usr/bin/env python3

from brain_games.engine import game
from brain_games.games.gcd import rule, gcd


def main():
    game(rule, gcd)


if __name__ == '__main__':
    main()
