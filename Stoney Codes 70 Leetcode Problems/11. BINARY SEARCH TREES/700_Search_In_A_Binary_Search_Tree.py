from typing import Optional

class Node:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def searchBST(root: Optional[Node], val: int) -> Optional[Node]:
    while (root is not None and root.val != val):
        if (val < root.val):
            root = root.left
        else:
            root = root.right
    return root

if __name__ == "__main__":
    root = Node(4)
    root.left = Node(2)
    root.right = Node(7)
    root.left.left = Node(1)
    root.left.right = Node(3)
    result = searchBST(root, 2)
    def Tree(node: Optional[Node]) -> list:
        if not node:
            return []
        return [node.val] + Tree(node.left) + Tree(node.right)
    print(Tree(result))

"""// Java Solution
class Solution {
    public TreeNode searchBST(TreeNode root, int val) {
        while (root != null && root.val != val) {
            root = val < root.val ? root.left : root.right;
        }
        return root;
    }
}"""