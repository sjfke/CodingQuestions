#!/usr/bin/env python3
#

# https://www.tutorialspoint.com/python/python_binary_tree.htm


class Node:

    def __init__(self, x):

        self.left = None
        self.right = None
        self.data = x

    def insert(self, x):
        # Compare the new value with the parent node
        if self.data:
            if x < self.data:
                if self.left is None:
                    self.left = Node(x)
                else:
                    self.left.insert(x)
            elif x > self.data:
                if self.right is None:
                    self.right = Node(x)
                else:
                    self.right.insert(x)
        else:
            self.data = x

    # Convert to a list
    def to_list(self, L):
        if self.left:
            self.left.to_list(L)

        L.append(self.data)

        if self.right:
            self.right.to_list(L)


def get_depth(root):
    if root is None:
        return 0
    return max(get_depth(root.left), get_depth(root.right)) + 1


if __name__ == "__main__":

    data = [1, 2, 3, 4]
    print('data: {0}'.format(data))
    tree = Node(data.pop(0))
    for val in data:
        tree.insert(val)

    L = []
    tree.to_list(L)
    print('heap: {0}'.format(L))
    print('depth: {0}'.format(get_depth(tree)))

    data = [1, 3, 6, 5, 9, 8]
    print('data: {0}'.format(data))
    tree = Node(data.pop(0))
    for val in data:
        tree.insert(val)

    L = []
    tree.to_list(L)
    print('heap: {0}'.format(L))
    print('depth: {0}'.format(get_depth(tree)))

    print('#')
    data = [3, 6, 9, 2, 15, 10, 14, 5, 12]
    print('data: {0}'.format(data))
    tree = Node(data.pop(0))
    for val in data:
        tree.insert(val)

    L = []
    tree.to_list(L)
    print('heap: {0}'.format(L))
    print('depth: {0}'.format(get_depth(tree)))
