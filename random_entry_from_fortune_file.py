#!/usr/bin/env python3
#
import os
import random
import re
import sys

# 1 https://github.com/bmc/fortunes
# 2 https://docs.python.org/3/library/random.html
# 3 https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# 4 https://docs.python.org/3/library/os.path.html#os.path.getsize
# 5 https://www.tutorialspoint.com/python3/python_reg_expressions.htm
# 6 https://python-notes.curiousefficiency.org/en/latest/python3/text_file_processing.html


def get_line_count(fd, strict=False):
    '''
    Get number of lines in file
    :param fd: file handle
    :param strict: only report non-empty lines
    '''
    line_count = 0
    current_offset = fd.tell()  # save file cursor
    fd.seek(0)
    for line in fd:
        if strict and line:
            line_count += 1
        else:
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


def get_fortune_text_from_list(fd, offset):
    '''
    Extract multi-line text from the file.
    :param fd: file handle
    :param offset: bytes from the begining of the file
    '''
    current_offset = fd.tell()  # save file cursor
    fd.seek(offset)
    cookie_text = fd.readline()

    # repeat..until loop
    while True:
        line = fd.readline()
        if not line:
            break
        elif re.match(r'^%$', line):
            break
        else:
            cookie_text += line

    fd.seek(current_offset)  # restore file cursor

    return cookie_text


def get_fortune_text_from_file(fd, offset):
    '''
    Extract multi-line cookie_text by searching the file
    :param fd: file handle
    :param offset: bytes from
    '''
    current_offset = fd.tell()
    fd.seek(offset)
    cookie_text = fd.readline()
    separator_found = False

    while True:
        line = fd.readline()
        if not line:
            break
        elif re.match(r'^%$', line):
            if not separator_found:
                # reject all text up until first separator found
                separator_found = True
                cookie_text = ''
            else:
                fd.seek(current_offset)  # restore file cursor
                return cookie_text
        else:
            cookie_text += line

    fd.seek(current_offset)  # restore file cursor
    return None


def get_file_size(textstr):
    '''
    Return file size in Bytes
    :param textstr: file name
    '''
    try:
        return os.path.getsize(textstr)
    except OSError as err:
        print("OS error: {0}".format(err))
        sys.exit(1)


if __name__ == '__main__':
    filename = 'fortunes'
    file_size = get_file_size(filename)

    with open(filename, 'r') as f:

        cookies = cookie_list(f)
        random_offset = random.randrange(len(cookies))
        # print('{0}, offset: {1} Bytes ({2} Bytes)'.format(filename, random_offset, file_size))
        cookie_text = get_fortune_text_from_list(f, cookies[random_offset])
        if not cookie_text:
            cookie_text = 'Not your lucky day, try again'

        print('list:')
        print('{0}'.format(cookie_text, end=''))

        random_offset = random.randrange(file_size)
        # print('{0}, offset: {1} Bytes ({2} Bytes)'.format(filename, random_offset, file_size))

        cookie_text = get_fortune_text_from_file(f, random_offset)
        if not cookie_text:
            cookie_text = 'Not your lucky day, try again'

        print('file:')
        print('{0}'.format(cookie_text, end=''))
