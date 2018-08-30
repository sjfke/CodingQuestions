#!/usr/bin/env python3


def number_of_subsets(L, desired_total):
    # print(L)
    # print(desired_total)
    return recursive(L, desired_total, len(L) - 1)


def recursive(L, desired_total, i):
    #     if desired_total == 16:
    #         print('L[i]: {0}; desired_total: {1}, i: {2}'.format(L[i], desired_total, i))

    if desired_total == 0:
        return 1  # empty set
    elif desired_total < 0:
        return 0  # not possible
    elif i < 0:
        return 0
    elif desired_total < L[i]:
        return recursive(L, desired_total, i - 1)  # desired_total is less than current array elelment
    else:
        # compute excluding and including the current array value
        return recursive(L, desired_total - L[i], i - 1) + recursive(L, desired_total, i - 1)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 10]
    total = 16
    print('answer: {0}'.format(number_of_subsets(arr, total)))
