from typing import Optional

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def getMinimumDifference(self, root: Optional[Node]) -> int:
        self.prev = float('-inf')
        self.min_diff = float('inf')

        def inorder(node: Node):
            if not node:
                return
            
            inorder(node.left)

            if self.prev != float('-inf'):
                diff = node.val - self.prev
                self.min_diff = min(self.min_diff, diff)
            
            self.prev = node.val
            inorder(node.right)

        inorder(root)
        return self.min_diff
    
if __name__ == "__main__":
    root = Node(4)
    root.left = Node(2)
    root.right = Node(6)
    root.left.left = Node(1)
    root.left.right = Node(3)
    print(Solution().getMinimumDifference(root))