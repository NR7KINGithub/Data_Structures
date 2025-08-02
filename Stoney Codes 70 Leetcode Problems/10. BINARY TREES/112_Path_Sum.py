from typing import Optional

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def hasPathSum(self, root: Optional[Node], targetSum: int) -> bool:
        def has_sum(root, cur_sum):
            if not root:
                return False
            
            cur_sum += root.val
            
            if not (root.left or root.right):
                return cur_sum == targetSum
            
            return has_sum(root.left, cur_sum) or has_sum(root.right, cur_sum)
        
        return has_sum(root, 0)
    
if __name__ == "__main__":
    root = Node(5)
    root.left = Node(4)
    root.right = Node(8)
    root.left.left = Node(11)
    root.right.left = Node(13)
    root.right.right = Node(4)
    root.left.left.left = Node(7)
    root.left.left.right = Node(2)
    root.right.right.right = Node(1)

    targetSum = 22

    print(Solution().hasPathSum(root, targetSum))