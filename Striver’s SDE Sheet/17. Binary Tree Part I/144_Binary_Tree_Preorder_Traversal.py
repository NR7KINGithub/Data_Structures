# Definition for a binary tree node
class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Function to initiate preorder traversal and return the resulting list
def preorderTraversal(root):
    # Create an empty list to store preorder traversal values
    arr = []
    # Call the preorder traversal function
    preorder(root, arr)
    # Return the resulting list containing preorder traversal values
    return arr

# Function to perform preorder traversal of the tree and store values in 'arr'
def preorder(root, arr):
    # If the current node is None(base case for recursion), return
    if root is None:
        return
    # Append the current node's value into the list
    arr.append(root.val)
    # Recursively traverse the left subtree
    preorder(root.left, arr)
    # Recursively traverse the right subtree
    preorder(root.right, arr)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(preorderTraversal(root))