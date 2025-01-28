# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Node, k: int) -> int:
        # Initialize variables to keep track of count and result
        self.count = 0
        self.result = None
        # Helper function for in-order traversal
        def in_order_traversal(node):
            if not node or self.result is not None:
                return   
            # Traverse the left subtree
            in_order_traversal(node.left)
            # Process the current node
            self.count += 1
            if self.count == k:
                self.result = node.val
                return
            # Traverse the right subtree
            in_order_traversal(node.right)
        # Perform the in-order traversal
        in_order_traversal(root)
        return self.result
    
if __name__ == "__main__":
    root = Node(3)
    root.left = Node(1)
    root.right = Node(4)
    root.left.right = Node(2)
    print(Solution().kthSmallest(root, 1))