#!/usr/bin/env python3
#


def balanced_checker(textstr):
    B = 0
    P = 0
    S = 0
    i = 0

    balanced = True
    for c in textstr:
        # print('c: {0}'.format(c))
        if c == '(':
            P += 1
        elif c == ')':
            if P > 0:
                P -= 1
            else:
                print("unbalanced: '{0}'".format(c))
                balanced = False

        if c == '{':
            B += 1
        elif c == '}':
            if B > 0:
                B -= 1
            else:
                print("unbalanced: '{0}'".format(c))
                balanced = False

        if c == ']':
            S += 1
        elif c == ']':
            if S > 0:
                S -= 1
            else:
                print("unbalanced: '{0}'".format(c))
                balanced = False

        i += 1

    return(balanced)


if __name__ == '__main__':
    data = []
    data.append('{([])}')
    data.append('()')
    data.append('()[]')

    for d in data:
        print("data:'{0}' => {1}".format(d, balanced_checker(d)))
