import random

# Creating node class

class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    # Function to insert in BST
    def insert(self, data):
        # if value is lesser than the value of the parent node
        if data < self.data:
            if self.leftChild:
                # if we still need to move towards the left subtree
                self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return
        # if value is greater than the value of the parent node
        else:
            if self.rightChild:
                # if we still need to move towards the right subtree
                self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return

    # Function to search in BST
    def search(self, val):
        # if value to be searched is found
        if val == self.data:
            return str(val) + " is found in the BST"
        # if value is lesser than the value of the parent node
        elif val < self.data:
            # if we still need to move towards the left subtree
            if self.leftChild:
                return self.leftChild.search(val)
            else:
                return str(val) + " is not found in the BST"
        # if value is greater than the value of the parent node
        else:
            # if we still need to move towards the right subtree
            if self.rightChild:
                return self.rightChild.search(val)
            else:
                return str(val) + " is not found in the BST"

                # function to print a BST
    def delete(self, val):
        if val < self.data:
            if self.leftChild:
                self.leftChild = self.leftChild.delete(val)
        elif val > self.data:
            if self.rightChild:
                self.rightChild = self.rightChild.delete(val)
        else:
            if self.leftChild is None and self.rightChild is None:
                return None
            if self.leftChild is None:
                return self.rightChild
            if self.rightChild is None:
                return self.leftChild
            min_val = self.rightChild.find_min()
            self.data = min_val
            self.rightChild = self.rightChild.delete(min_val)
        return self

    def find_min(self):
        current = self
        while current.leftChild:
            current = current.leftChild
        return current.data
    def PrintTree(self):
        if self.leftChild:
            self.leftChild.PrintTree()
        print(self.data),
        if self.rightChild:
            self.rightChild.PrintTree()


arr = [random.randint(1, 20) for _ in range(20)]

# Creating root node
root = Node(arr[0])
# Inserting values in BST
for i in range(1, len(arr)):
    root.insert(arr[i])
# searching the values
target = arr[random.randint(0,19)]

print(root.search(target))
root.PrintTree()
root.delete(5)
print("-------------")
root.PrintTree()