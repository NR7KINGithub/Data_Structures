from typing import Optional

# Definition for a binary tree node
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root: Optional[Node]) -> int:
    longest = [0]
    
    def dfs(root):
        if not root:
            return 0
        
        left_height = dfs(root.left)
        right_height = dfs(root.right)
        diameter = left_height + right_height
        longest[0] = max(longest[0], diameter)
        return 1 + max(left_height, right_height)
    
    dfs(root)
    return longest[0]

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print(diameterOfBinaryTree(root))