# Definition for a binary tree node
class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Function to initiate inorder traversal and return the resulting list
def inorderTraversal(root):
    # Create an empty list to store inorder traversal values
    arr = []
    # Call the inorder traversal function
    inorder(root, arr)
    # Return the resulting list containing inorder traversal values
    return arr

# Function to perform inorder traversal of the tree and store values in 'arr'
def inorder(root, arr):
    # If the current node is None(base case for recursion), return
    if root is None:
        return
    # Recursively traverse the left subtree
    inorder(root.left, arr)
    # Append the current node's value into the list
    arr.append(root.val)
    # Recursively traverse the right subtree
    inorder(root.right, arr)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(inorderTraversal(root))