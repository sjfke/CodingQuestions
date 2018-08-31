#!/usr/bin/env python3
#

# https://practice.geeksforgeeks.org/problems/kadanes-algorithm/0
# https://www.puzzlr.org/understanding-kadanes-algorithm-maximum-subarray-problem/


def max_sublist(L):
    if len(L) == 0:
        return None
    else:
        running_total = L[0]
        max_found = L[0]
        result = []
        running_list = []
        running_list.append(L[0])
        for x in L[1:]:
            running_total += x
            if (running_total > 0):
                running_list.append(x)
                if running_total > max_found:
                    max_found = running_total
                    result = running_list.copy()
            else:
                running_total = x
                running_list = []
                running_list.append(x)

        return {'max': max_found, 'list': result}


if __name__ == "__main__":
    data = []
    data.append([3, 5, -2, -1, 5, 3, 1, -4, -6, -5])
    data.append([3, 5, -2, -1, 5, 3, 1, -4, -6, -5, 11, 10, 6])

    for d in data:
        print('data: {0} => {1}'.format(d, max_sublist(d)))
