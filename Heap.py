#!/usr/bin/env python3
#

# https://www.tutorialspoint.com/python/python_binary_tree.htm

class Heap:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
    # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Heap(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Heap(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print('{0:2d}'.format(self.data), end='')
        
        if self.right:
            self.right.PrintTree()
            
            
            
if __name__ == "__main__":
    data = [1, 3, 6, 5, 9, 8]
    print('data: {0}'.format(data))
    value = data.pop(0)
    root = Heap(value)
    for val in data:
        root.insert(val)
    
    print('heap: [', end='')
    root.PrintTree()
    print(']')
