#!/usr/bin/env python3
#

# https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s/0

# 1 3 5 2 2 => 3 (value =5 = (1+3) = (2+2))


def equilibrium_point(L):
    result = {'point': -1, 'value': None}

    if len(L) == 0:
        return -1
    if len(L) == 1:
        return 1
    else:
        max_index = len(L) - 1
        for i in range(1, max_index):
            if sum(L[0:i]) == sum(L[i + 1:]):
                result['point'] = i + 1
                result['value'] = L[i]

    return {'index': result['point'], 'value': result['value']}


if __name__ == "__main__":
    data = []
    data.append([2])
    data.append([1])
    data.append([5])
    data.append([1, 3, 5, 2, 2])
    data.append([1, 3, 5, 4])
    data.append([4, 5, 4])
    data.append([1, 2, 5, 4])
    data.append([2, 2, 5, 4])
    data.append([1, 1])
    data.append([])

    for d in data:
        print('data: {0} => {1}'.format(d, equilibrium_point(d)))
