# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
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
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)
    print(Solution().kthSmallest(root, 1))