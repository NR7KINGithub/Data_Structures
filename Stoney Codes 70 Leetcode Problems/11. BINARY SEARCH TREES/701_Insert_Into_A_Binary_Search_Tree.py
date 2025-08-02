from typing import Optional

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def insertIntoBST(self, root: Optional[Node], val: int) -> Optional[Node]:
        insert = Node(val)
        current = root

        if not root:
            return insert

        while True:
            if current.val > val:
                if current.left:
                    current = current.left
                else:
                    current.left = insert
                    break
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = insert
                    break

        return root
    
if __name__ == "__main__":
    root = Node(4)
    root.left = Node(2)
    root.right = Node(7)
    root.left.left = Node(1)
    root.left.right = Node(3)
    val = 5
    result = Solution().insertIntoBST(root, val)
    
    def Tree(node: Optional[Node]) -> list:
        if not node:
            return []
        return [node.val] + Tree(node.left) + Tree(node.right)
    print(Tree(result))

"""// Java Solution
class Solution {
    public TreeNode insertIntoBST(TreeNode root, int val) {
        TreeNode insert = new TreeNode(val);
        TreeNode current = root;

        if (root == null) {
            return insert;
        }

        while (true) {
            if (current.val > val) {
                if (current.left != null) {
                    current = current.left;
                }
                else {
                    current.left = insert;
                    break;
                }
            }
            else {
                if (current.right != null) {
                    current = current.right;
                }
                else {
                    current.right = insert;
                    break;
                }
            }
        } 
        return root;
    }
}"""