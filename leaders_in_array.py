#!/usr/bin/env python3
#

# https://practice.geeksforgeeks.org/problems/leaders-in-an-array/0
# 16 17 4 3 5 2 => 17 5 2
# 1 2 3 4 0     => 4 0
# 5             =>  7 7 3
# 16            => 16
# 16 2          => 16 2


def find_leaders_in_array_iterative(v, L):
    sequence = []
    x = v
    for i in L:
        if x > i:
            sequence.append(x)
        x = i

    sequence.append(L[-1])
    return sequence


def find_leaders_in_array_recursive(v, L, S):
    #     print('v: {0}, L: {1}, S: {2}'.format(v, L, S))
    if len(L) == 0:
        S.append(v)
    elif v > L[0]:
        S.append(v)
        find_leaders_in_array_recursive(L[0], L[1:], S)
    else:
        find_leaders_in_array_recursive(L[0], L[1:], S)


def leaders_in_array_iterative(L):
    if len(L) == 0:
        return None
    elif len(L) == 1:
        return L
    else:
        sequence = []
        sequence = find_leaders_in_array_iterative(L[0], L[1:])
        return sequence


def leaders_in_array_recursive(L):
    if len(L) == 0:
        return None
    elif len(L) == 1:
        return L
    else:
        sequence = []
        find_leaders_in_array_recursive(L[0], L[1:], sequence)
        return sequence


if __name__ == '__main__':
    data = []
    data.append([16, 17, 4, 3, 5, 2])
    data.append([1, 2, 3, 4, 0])
    data.append([5])
    data.append([16, 2])
    data.append([])

    heading = 'Iterative'
    print(heading)
    print('=' * len(heading))
    for d in data:
        print('data: {0} => {1}'.format(d, leaders_in_array_iterative(d)))

    heading = 'Recursive'
    print(heading)
    print('=' * len(heading))
    for d in data:
        print('data: {0} => {1}'.format(d, leaders_in_array_recursive(d)))
