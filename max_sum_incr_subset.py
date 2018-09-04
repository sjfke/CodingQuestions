#!/usr/bin/env python3
#

# https://practice.geeksforgeeks.org/problems/maximum-sum-increasing-subsequence/0

# 1 101 2 3 100 4 5
# All the increasing subsequences : (1,101); (1,2,3,100); (1,2,3,4,5), out of this (1,2,3,100)
# Need to find subsets: [1,101], [1,2,3,100], [1,2,3,4,5] implies recursive or iterative


def recursion(v, L, sequence, array_of_sequences):
    #     print('Down: {0}, List: {1}'.format(v, L))
    if len(L) == 0:
        return False
    elif len(L) == 1:
        x = L[0]
        sequence.append(v)
        sequence.append(x)
        # print(sequence)
        array_of_sequences.append(sequence.copy())
    elif len(L) > 1:
        x = L[0]
        sequence.append(v)
        if v > x:
            # print(sequence)
            array_of_sequences.append(sequence.copy())
            sequence.pop()

        if recursion(x, L[1:], sequence, array_of_sequences):
            return False
    else:
        return True


def iteration(L):
    array_of_sequences = []
    val = L[0]
    sequences = [val]
    lastval = sequences[-1]
    for j in L[1:]:
        newval = j
        if L[-1] == newval:
            # save last sequence
            sequences.append(newval)
            S = sequences.copy()
            array_of_sequences.append(S)
        elif lastval < newval:
            # sequence ascending
            sequences.append(newval)
            lastval = newval
        else:
            if len(sequences) > 1:
                # need to save sequence and start a new one
                S = sequences.copy()
                array_of_sequences.append(S)
                sequences.pop()
                lastval = sequences[-1]
                sequences.append(newval)
                lastval = newval

    result = {'sum': 0, 'sequence': None}
    # compute the highest value
    for x in array_of_sequences:
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
        return (iteration(L))


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

    # compute the highest value
    result = {'sum': 0, 'sequence': None}
    for x in array_of_sequences:
        total = sum(x)
        if total > result['sum']:
            result['sum'] = total
            result['sequence'] = x

    return(result)


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
