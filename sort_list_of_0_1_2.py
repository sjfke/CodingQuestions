#!/usr/bin/env python3
#

# https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s/0


def sorted_sublist(L):
    local_list = sorted(L.copy())
    if local_list[0] < 0 or local_list[-1] > 2:
        return None
    else:
        return local_list


if __name__ == "__main__":
    data = []
    data.append([2])
    data.append([5])
    data.append([0, 2, 1, 2, 0])
    data.append([3])
    data.append([0, 1, 0])

    for d in data:
        print('data: {0} => {1}'.format(d, sorted_sublist(d)))
