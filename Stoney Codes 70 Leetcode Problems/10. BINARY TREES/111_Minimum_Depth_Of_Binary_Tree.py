from typing import Optional

# Definition for a binary tree node
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[Node]) -> int:
        if not root:
            return 0
        
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        if not root.left:
            return right + 1
        if not root.right:
            return left + 1

        return 1 + min(left, right)

if __name__ == "__main__":
    root = Node(3)
    root.left = Node(9)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.right = Node(7)

    print(Solution().minDepth(root))

"""// Java Solution
class Solution {
    public int minDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int left = minDepth(root.left);
        int right = minDepth(root.right);

        if (root.left == null) {
            return right + 1;
        }
        if (root.right == null) {
            return left + 1;
        }
        return 1 + Math.min(left, right);
    }
}"""