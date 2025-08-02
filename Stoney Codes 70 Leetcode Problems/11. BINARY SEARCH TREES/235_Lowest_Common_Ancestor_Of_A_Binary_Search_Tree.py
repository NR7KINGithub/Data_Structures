class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'Node', p: 'Node', q: 'Node') -> 'Node':
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root
        
if __name__ == "__main__":
    p = Node(2)
    q = Node(8)
    root = Node(6)
    root.left = p
    root.right = q
    root.left.left = Node(0)
    root.left.right = Node(8)
    root.right.left = Node(7)
    root.right.right = Node(9)
    root.left.right.left = Node(3)
    root.left.right.right = Node(5)
    lca = Solution().lowestCommonAncestor(root, p, q)
    print(lca.val)

"""// Java Solution
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        while (root != null) {
            if (p.val < root.val && q.val < root.val) {
                root = root.left;
            } else if (p.val > root.val && q.val > root.val) {
                root = root.right;
            } else {
                return root;
            }
        }
        return null;
    }
}"""