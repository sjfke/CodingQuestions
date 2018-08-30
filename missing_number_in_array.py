#!/usr/bin/env python3
#


def find_missing_numbers(L):
    ''' find the missing number in an unsorted list of integers'''
    # dedupe into a dictionary and find min/max
    limits = {'min': None, 'max': None}
    D = {}
    for x in L:
        if limits['min'] is None or x < limits['min']:
            limits['min'] = x
        if limits['max'] is None or x > limits['max']:
            limits['max'] = x

        if x in D:
            D[x] += 1
        else:
            D[x] = 1

    # find missing numbers
    result = []
    for i in range(limits['min'], limits['max']):
        if not i in D:
            result.append(i)

    return result


if __name__ == "__main__":
    data = []
    data.append([1, 2, 3, 5])
    data.append([1, 2, 3, 5, 6, 7, 8, 10])
    data.append([10, 2, 3, 5, 6, 7, 8])
    data.append([2])
    data.append([5])
    data.append([-3, 2, 3, 5, 6, 7, 8, 10])

    for d in data:
        print('data: {0} => {1}'.format(d, find_missing_numbers(d)))
