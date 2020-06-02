# from binary_search_tree import binary_search_tree
import time
# import sys
# sys.path.append('./binary_search_tree.py')


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # recursive
    # Insert the given value into the tree
    def insert(self, value):
        # check if empty
        if value is None:
            return
        # then assigin new node value
        elif self.value is None:
            self.value = BSTNode(value)
        # check if new value is less than current node value
        elif value < self.value:
            # and check if there is no left value
            if not self.left:
                # assign new left node as new node value
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        # otherwise if it is greater than current node
        else:
            # check if there is no right value
            if not self.right:
                # assign new right node as new value
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # recursive
        # check if initial value is target value
        if self.value == target:
            return True
        # if value is greater than target then look left
        if self.value > target:
            # if target is on the left return True
            if self.left:
                return self.left.contains(target)
        # if value is less than target the look right
        elif self.value < target:
            # if target is on the right return True
            if self.right:
                return self.right.contains(target)
        # otherwise if not found then return False
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        # recursive
        # if there is no value to the right return current value as the right most highest value
        if not self.right:
            return self.value
        return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # recursive
        # pass a value in function call
        fn(self.value)
        # if there is a left, recurse to the left and call value
        if self.left:
            self.left.for_each(fn)
        # if there is a right, recurse to the right and call value
        if self.right is not None:
            self.right.for_each(fn)


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure
bst = BSTNode(names_2[1])  # use BST for names in names_2
# Replace the nested for loops below with your improvements
for name1 in names_1:
    bst.insert(name1)

for name2 in names_2:
    if bst.contains(name2):
        duplicates.append(name2)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
