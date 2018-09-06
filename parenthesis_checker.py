#!/usr/bin/env python3
#


def balanced_checker(textstr):
    brackets = {'braces': 0, 'parenthesis': 0, 'square': 0}
    i = 1

    for c in textstr:
        # print('c: {0}'.format(c))
        if c == '(':
            brackets['parenthesis'] += 1
        elif c == ')':
            if brackets['parenthesis'] > 0:
                brackets['parenthesis'] -= 1
            else:
                print('{0:4s}: {1}'.format('()', '^' * i))

        if c == '{':
            brackets['braces'] += 1
        elif c == '}':
            if brackets['braces'] > 0:
                brackets['braces'] -= 1
            else:
                print('{0:4s}: {1}'.format('{}', '^' * i))

        if c == ']':
            brackets['square'] += 1
        elif c == ']':
            if brackets['square'] > 0:
                brackets['square'] -= 1
            else:
                print('{0:4s}: {1}'.format('[]', '^' * i))

        i += 1

    return(brackets['braces'] == 0 and brackets['parenthesis'] == 0 and brackets['square'] == 0)


if __name__ == '__main__':
    data = []
    data.append('{([])}')
    data.append('{()[])}')
    data.append('{()}')
    data.append('()')
    data.append('()[]')
    data.append('{}([[])}')

    for d in data:
        print("data:'{0}'".format(d))
        balanced_checker(d)
