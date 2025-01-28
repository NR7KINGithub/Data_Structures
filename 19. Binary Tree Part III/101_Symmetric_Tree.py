# Definition for a binary tree node
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root):
    def Symmetric(root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False
        return Symmetric(root1.left, root2.right) and \
                Symmetric(root1.right, root2.left)
    return Symmetric(root,root)
    

root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.right.right = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)

print(isSymmetric(root))