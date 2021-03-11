
"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

from collections import deque

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if target > self.value and self.right:
            return self.right.contains(target)
        elif target < self.value and self.left:
            return self.left.contains(target)
        else: return False

    def __contains__(self, target):
        return (
            self.value == target
            or (self.left and target in self.left)
            or (self.right and target in self.right)
        )


    # Return the maximum value found in the tree
    def get_max(self):
        current = self
        while current.right:
            current = current.right
        return current.value
    
    def get_max_recursive(self):
        if self.right is None:
            return self.value
        else: return self.right.get_max_recursive()


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)
        

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_dft(self):
        if self.left:
            self.left.in_order_dft()
        
        print(self.value)
        
        if self.right:
            self.right.in_order_dft()
        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        q = deque()
        q.append(self)
        while len(q) != 0:
            current = q.popleft()
            print(current.value)
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        stack = deque()
        stack.append(self)
        while stack:
            current = stack.pop()
            print(current.value)
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)


    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        print(self.value)
        if self.left:
            self.left.pre_order_dft()
        if self.right:
            self.right.pre_order_dft()

    # Print Post-order recursive DFT
    def post_order_dft(self):
        if self.left:
            self.left.pre_order_dft()
        if self.right:
            self.right.pre_order_dft()
        print(self.value)

        


if __name__=="__main__" :
    
    """
    This code is necessary for testing the `print` methods
    """
    bst = BSTNode(1)

    bst.insert(8)
    bst.insert(5)
    bst.insert(7)
    bst.insert(6)
    bst.insert(3)
    bst.insert(4)
    bst.insert(2)

    def print_times_2(value):
        print(value * 2)

    bst.for_each(print_times_2)
    bst.bft_print()
    bst.dft_print()

    print("elegant methods")
    print("pre order")
    bst.pre_order_dft()
    print("in order")
    bst.in_order_dft()
    print("post order")
    bst.post_order_dft()  
