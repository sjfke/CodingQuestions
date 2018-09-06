#!/usr/bin/env python3
#

# https://practice.geeksforgeeks.org/problems/maximum-sum-increasing-subsequence/0

# 1 101 2 3 100 4 5
# All the increasing subsequences : (1,101); (1,2,3,100); (1,2,3,4,5), out of this (1,2,3,100)
# Need to find subsets: [1,101], [1,2,3,100], [1,2,3,4,5] implies recursive or iterative


def recursion(v, L, sequence, array_of_sequences):
    # print('v: {0}, L: {1}, S: {2}, AS: {3}'.format(v, L, sequence, array_of_sequences))
    if len(L) == 0:
        sequence.append(v)
        array_of_sequences.append(sequence.copy())
        # print('v: {0}, L: {1}, S: {2}, AS: {3}'.format(v, L, sequence, array_of_sequences))
    elif v < L[0]:
        sequence.append(v)
        recursion(L[0], L[1:], sequence, array_of_sequences)
    else:
        sequence.append(v)
        array_of_sequences.append(sequence.copy())
        sequence.pop()
        recursion(L[0], L[1:], sequence, array_of_sequences)


def iteration(v, L):
    sequence = []
    array_of_sequences = []
    sequence.append(v)
    for i in L:
        if i > sequence[-1]:
            sequence.append(i)
        else:
            array_of_sequences.append(sequence.copy())
            sequence.pop()
            sequence.append(i)

    array_of_sequences.append(sequence.copy())
    return(array_of_sequences)


def find_max_sum_and_sequence(L):
    result = {'sum': 0, 'sequence': None}
    for x in L:
        total = sum(x)
        if total > result['sum']:
            result['sum'] = total
            result['sequence'] = x

    return(result)


def max_sum_subset_iterative(L):
    if len(L) == 0:
        return None
    if len(L) == 1:
        return L[1]
    else:
        array_of_sequences = iteration(L[0], L[1:])
        # print(array_of_sequences)
        return(find_max_sum_and_sequence(array_of_sequences))


def max_sum_subset_recursive(L):
    if len(L) == 0:
        return None
    elif len(L) == 1:
        total = L[0]
        return {'sum': total, 'sequence': L}

    sequence = []
    array_of_sequences = []
    recursion(L[0], L[1:], sequence, array_of_sequences)

    # print(array_of_sequences)
    return(find_max_sum_and_sequence(array_of_sequences))


if __name__ == "__main__":
    data = []
    data.append([1, 101, 2, 3, 100, 4, 5])
    data.append([])

    heading = 'Iterative'
    print(heading)
    print('=' * len(heading))
    for d in data:
        print('data: {0} => {1}'.format(d, max_sum_subset_iterative(d)))

    heading = 'Recursive'
    print(heading)
    print('=' * len(heading))
    for d in data:
        print('data: {0} => {1}'.format(d, max_sum_subset_recursive(d)))
