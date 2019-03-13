"""
A small generator to randomly generate silly names from two tuples.

The goal of this script is to conform to PEP 8 and PEP 257 and achieve
a rating of 10/10 when running pylint on this file.
"""

import sys
import random


def main():
    """Choose names at random from two tuples and print to screen."""
    print("Welcome to the 'Game of Thrones Name Picker'\n")
    print("A name that GRRM might come up with:\n")

    with open('asoiaf_first_names.txt') as first_name_input:
        first_names = [line[:-1] for line in first_name_input]

    with open('asoiaf_last_names.txt') as last_name_input:
        last_names = [line[:-1] for line in last_name_input]

    while True:
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)

        print('\n')
        print(f'{first_name} {last_name}', file=sys.stderr)
        print('\n')

        try_again = input("Try again? (Press Enter else 'n' to quit)\n")
        if try_again.lower() == 'n':
            break


if __name__ == '__main__':
    main()
