#!/usr/bin/env python3

from brain_games.engine import game
from brain_games.games.even import rule, even


def main():
    game(rule, even)


if __name__ == '__main__':
    main()
