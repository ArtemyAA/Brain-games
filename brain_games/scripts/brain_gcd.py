#!/usr/bin/env python3


from brain_games.games import gcd
from brain_games import engine


def main():
    engine.start(gcd)


if __name__ == '__main__':
    main()