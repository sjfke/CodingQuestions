#!/usr/bin/env python3


def add_one_to_list(L):
    ''' add 1 to list, handling carry etc'''
    # create list of zero's
    length = len(arr)
    result = [0] * length
    carry = 1

    for i in range(len(L) - 1, -1, -1):
        # print('i: {0}'.format(i))
        numsum = L[i] + carry

        if numsum == 10:
            carry = 1
        else:
            carry = 0

        result[i] = numsum % 10

    if carry == 1:
        result.insert(0, 1)

    return result


def incr_array(L):
    '''convert to integer add 1, convert back to a list'''
    numstr = ''.join(map(str, L))
    result = []
    for i in str(int(numstr) + 1):
        result.append(int(i))
    return result


if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    arr = [9, 9, 9]
    print('before: {0}'.format(arr))
    print('after : {0}'.format(add_one_to_list(arr)))
    print('after2: {0}'.format(incr_array(arr)))
