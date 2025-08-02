# Definition for a binary tree node
class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Function to initiate postorder traversal and return the resulting list
def postorderTraversal(root):
    # Create an empty list to store postorder traversal values
    arr = []
    # Call the postorder traversal function
    postorder(root, arr)
    # Return the resulting list containing postorder traversal values
    return arr

# Function to perform postorder traversal of the tree and store values in 'arr'
def postorder(root, arr):
    # If the current node is None(base case for recursion), return
    if root is None:
        return
    # Recursively traverse the left subtree
    postorder(root.left, arr)
    # Recursively traverse the right subtree
    postorder(root.right, arr)
    # Append the current node's value into the list
    arr.append(root.val)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(postorderTraversal(root))