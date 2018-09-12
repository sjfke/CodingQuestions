#!/usr/bin/env python3
#
import os
import sys

# https://github.com/bmc/fortunes
# https://docs.python.org/3/library/random.html
# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# https://docs.python.org/3/library/os.path.html#os.path.getsize


def get_line_count(fd):
    line_count = 0
    for line in fd:
        # print(line, end='')
        line_count += 1

    return line_count


def coookie_list(fd):
    L = []
    # %
    # "Acting is an art which consists of keeping the audience from coughing."
    # %
    # "Anchovies? You've got the wrong man! I spell my name DANGER! (click)"
    # %
    # "Benson, you are so free of the ravages of intelligence."
    #         ― Time Bandits
    # %

    for line in fd:
        print(line, end='')
    return L


if __name__ == '__main__':
    filename = 'fortunes'

    file_size = None
    try:
        file_size = os.path.getsize(filename)
    except OSError as err:
        print("OS error: {0}".format(err))
        sys.exit(1)

    with open(filename) as f:

        print("'{0}', has {1:3d} lines ({2} Bytes)".format(filename, get_line_count(f), file_size))
