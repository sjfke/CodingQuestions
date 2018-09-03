#!/usr/bin/env python3
#

# https://practice.geeksforgeeks.org/problems/maximum-sum-increasing-subsequence/0

# 1 101 2 3 100 4 5
# All the increasing subsequences : (1,101); (1,2,3,100); (1,2,3,4,5), out of this (1,2,3,100)
# Need to find subsets: [1,101], [1,2,3,100], [1,2,3,4,5] implies recursive or iterative


def recursion(L, i, l, AS, S):
    if len(L) == 0:
        return None
    elif i > len(L):
        return False
    if i == l:
        return True
    else:

        print(AS)
        print(S)
        print('L: {0}, {1}'.format(L, i))
        curnum = L[i]
        nextnum = L[i + 1]
        if nextnum > curnum:
            recursion(L, i + 1, l, AS, S)
        else:
            recursion(L, i + 2, l, AS, S)


def iteration(L):
    array_of_sequences = []
    val = L[0]
    sequences = [val]
    lastval = sequences[-1]
    for j in L[1:]:
        newval = j
        # print('val:{0}, lastval:{1}, newval: {2}'.format(val, lastval, newval))
        if L[-1] == newval:
            sequences.append(newval)
            T = sequences.copy()
            # print('Sequence {0}'.format(sequences))
            array_of_sequences.append(T)
        elif lastval < newval:
            sequences.append(newval)
            # print('Append {0} <= {1}; sequences: {2}'.format(val, newval, sequences))
            lastval = newval
        else:
            if len(sequences) > 1:
                # print('Pop: {0}'.format(lastval))
                T = sequences.copy()
                # print('Sequence {0}'.format(sequences))
                array_of_sequences.append(T)
                sequences.pop()
                # print('Poping {0}; sequences: {1}'.format(lastval, sequences))
                lastval = sequences[-1]
                sequences.append(newval)
                # print('Popend {0} <= {1}; sequences: {2}'.format(val, newval, sequences))
                lastval = newval

    result = {'sum': 0, 'sequence': None}
    for x in array_of_sequences:
        total = sum(x)
        if total > result['sum']:
            result['sum'] = total
            result['sequence'] = x

    return(result)


def max_sum_subset(L):
    if len(L) == 0:
        return None
    if len(L) == 1:
        return L[1]
    else:
        return (iteration(L))


if __name__ == "__main__":
    data = []
    data.append([1, 101, 2, 3, 100, 4, 5])
    data.append([])

    for d in data:
        print('data: {0} => {1}'.format(d, max_sum_subset(d)))
