#!/usr/bin/env python3

from brain_games.engine import game
from brain_games.games.progression import rule, progression


def main():
    game(rule, progression)


if __name__ == '__main__':
    main()
