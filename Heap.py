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

    # Convert to a list
    def to_list(self, L):
        if self.left:
            self.left.to_list(L)

        L.append(self.data)
        
        if self.right:
            self.right.to_list(L)
            
            
            
if __name__ == "__main__":
    data = [1, 3, 6, 5, 9, 8]
    print('data: {0}'.format(data))
    root = Heap(data.pop(0))
    for val in data:
        root.insert(val)
    
    L = []
    root.to_list(L)
    print('heap: {0}'.format(L))

    print('#')
    data = [3, 6, 9, 2, 15, 10, 14, 5, 12]
    print('data: {0}'.format(data))
    root = Heap(data.pop(0))
    for val in data:
        root.insert(val)
    
    L = []
    root.to_list(L)
    print('heap: {0}'.format(L))
    
    
