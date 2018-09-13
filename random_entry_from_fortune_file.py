#!/usr/bin/env python3
#
import os
import random
import re
import sys
import locale

# 1 https://github.com/bmc/fortunes
# 2 https://docs.python.org/3/library/random.html
# 3 https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# 4 https://docs.python.org/3/library/os.path.html#os.path.getsize
# 5 https://www.tutorialspoint.com/python3/python_reg_expressions.htm
# 6 https://python-notes.curiousefficiency.org/en/latest/python3/text_file_processing.html


def get_line_count(fd):
    line_count = 0
    current_offset = fd.tell()  # save file cursor
    fd.seek(0)
    for line in fd:
        # print(line, end='')
        line_count += 1

    fd.seek(current_offset)  # restore file cursor
    return line_count


def cookie_list(fd):
    '''
    Build a list of separator offset locations
    :param fd: file handle
    '''

    # %
    # "Acting is an art which consists of keeping the audience from coughing."
    # %
    # "Anchovies? You've got the wrong man! I spell my name DANGER! (click)"
    # %
    # "Benson, you are so free of the ravages of intelligence."
    #         ― Time Bandits
    # %

    current_offset = fd.tell()  # save file cursor
    fd.seek(0)  # start at the first byte

    L = []

    # Cannot use for..loop and .tell() method
    while True:
        line = fd.readline()
        if not line:
            break

        # Record offset of separator
        if re.match(r'^%$', line):
            L.append(fd.tell())

    fd.seek(current_offset)  # restore file cursor
    return L


def get_fortune_text(fd, offset):
    '''
    Extract lulti-line text from the file.
    :param fd: file handle
    :param offset: bytes from the begining of the file
    '''
    current_offset = fd.tell()
    fd.seek(offset)
    cookie_text = fd.readline()

    while True:
        line = fd.readline()
        if not line:
            break
        elif re.match(r'^%$', line):
            break
        else:
            cookie_text += line

    fd.seek(current_offset)

    return cookie_text


if __name__ == '__main__':
    filename = 'fortunes'

    file_size = None
    try:
        file_size = os.path.getsize(filename)
    except OSError as err:
        print("OS error: {0}".format(err))
        sys.exit(1)

    with open(filename, 'r') as f:

        cookies = cookie_list(f)
        random_offset = random.randrange(len(cookies))
        print(get_fortune_text(f, cookies[random_offset]), end='')

#         print('{0}'.format(cookies))
#         print("'{0}', has {1:3d} lines ({2} Bytes)".format(filename, get_line_count(f), file_size))
