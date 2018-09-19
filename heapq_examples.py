#!/usr/bin/env python3
#
import heapq

# https://docs.python.org/3.0/library/heapq.html

if __name__ == "__main__":

    heap = []
    data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]

    for item in data:
        heapq.heappush(heap, item)

    print('#')
    print('heap: {0}'.format(heap))
    print('nlargest(1): {0}'.format(heapq.nlargest(1, heap)))
    print('nlargest(3): {0}'.format(heapq.nlargest(3, heap)))
    print('nsmallest(1): {0}'.format(heapq.nsmallest(1, heap)))
    print('nsmallest(3): {0}'.format(heapq.nsmallest(3, heap)))

    ordered = []
    while heap:
        ordered.append(heapq.heappop(heap))

    print('ordered: {0}'.format(ordered))

    heap2 = [11, 3, 15, 7, 9, 23, 4, 6, 8, 10]
    heapq.heapify(heap2)
    print('#')
    print('heap2: {0}'.format(heap2))
    print('nlargest(1): {0}'.format(heapq.nlargest(1, heap2)))
    print('nlargest(3): {0}'.format(heapq.nlargest(3, heap2)))
    print('nsmallest(1): {0}'.format(heapq.nsmallest(1, heap2)))
    print('nsmallest(3): {0}'.format(heapq.nsmallest(3, heap2)))

    data = [(1, 'J'), (4, 'N'), (3, 'H'), (2, 'O')]
    for item in data:
        heapq.heappush(heap, item)

    print('#')
    print('heap: {0}'.format(heap))
    print('nlargest(1): {0}'.format(heapq.nlargest(1, heap)))
    print('nlargest(3): {0}'.format(heapq.nlargest(3, heap)))
    print('nsmallest(1): {0}'.format(heapq.nsmallest(1, heap)))
    print('nsmallest(3): {0}'.format(heapq.nsmallest(3, heap)))
