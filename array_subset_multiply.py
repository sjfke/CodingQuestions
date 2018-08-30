#!/usr/bin/env python3


def solution1(L, desired_number):
    ''' simple approach with duplicates'''
    result = []

    for i in L:
        num = int(desired_number / i)
        if num in L:
            pair = [i, num]
            result.append(pair)

    return result


def solution2(L, desired_number):
    '''simple approach without duplicates'''
    result = []
    matched = {}

    for i in L:
        num = int(desired_number / i)
        if num in L:
            pair = [i, num]
            if not (i in matched or num in matched):
                matched[num] = 1
                result.append(pair)

    return result


def solution3(L, desired_number):
    '''prettier approach without duplicates'''
    result = []
    matched = {}

    for i in L:
        num = int(desired_number / i)
        if num in L:
            if (num > i):
                pair = [i, num]
            else:
                pair = [num, i]

            if not (i in matched or num in matched):
                matched[num] = 1
                result.append(pair)

    return result


def solution4(L, desired_number):
    '''iterate over top-level and recurse to find multiply matches'''
    if len(L) == 0:
        return None
    elif desired_number == 0:
        return None
    else:
        result = []
        matched = {}

        for i in range(0, len(L) - 1):
            recursive(result, matched, L[i:], desired_number, L[i])

        return result


def recursive(result, matched, L, desired_number, value):

    if len(L) == 0:
        return None

    elif value * L[0] == desired_number:
        pair = []
        # print('recursion: {0}: {0} x {1} = {2}'.format(value, L[0], desired_number))
        if (value > L[0]):
            pair = [L[0], value]
        else:
            pair = [value, L[0]]

        # print('recursion: {0}'.format(pair))
        key = ','.join(map(str, pair))
        if not (key in matched):
            result.append(pair)
            matched[key] = 1

    elif len(L) > 0:
        recursive(result, matched, L[1:], desired_number, value)

        #print('{0}: {1}'.format(L[0], L))
    return result


def solution5(L, desired_number):
    '''fully recursive approach'''

    if not L:
        return None
    elif desired_number == 0:
        return None
    else:
        result = []
        matched = {}
        recurse50(result, matched, L, desired_number)

        return result


def recurse50(result, matched, L, desired_number):
    if len(L) == 0:
        return None
    else:
        value = L.pop()
        L2 = L.copy()
        recurse51(result, matched, L2, desired_number, value)
        recurse50(result, matched, L2, desired_number)
        return result


def recurse51(result, matched, L, desired_number, value):

    if len(L) == 0:
        return None

    elif value * L[0] == desired_number:
        pair = []
        #print('recursion: {0}: {0} x {1} = {2}'.format(value, L[0], desired_number))
        if (value > L[0]):
            pair = [L[0], value]
        else:
            pair = [value, L[0]]

        #print('recursion: {0}'.format(pair))
        key = ','.join(map(str, pair))
        if not (key in matched):
            result.append(pair)
            matched[key] = 1

    elif len(L) > 0:
        value = L.pop(0)
        L2 = L.copy()
        recurse51(result, matched, L2, desired_number, value)
        #print('{0}: {1}'.format(value, L))
    return result


if __name__ == "__main__":
    total = 20
    arr = [5, 2, 4, 1, 6, 5, 5, 4, 40, 10, -1]
    print('array data         : {0}'.format(arr))
    print('simple + duplicates: {0}'.format(solution1(arr, total)))
    print('simple - duplicates: {0}'.format(solution2(arr, total)))
    print('better - duplicates: {0}'.format(solution3(arr, total)))
    print('loop + recursion: {0}'.format(solution4(arr, total)))
    print('double recursion: {0}'.format(solution5(arr, total)))
