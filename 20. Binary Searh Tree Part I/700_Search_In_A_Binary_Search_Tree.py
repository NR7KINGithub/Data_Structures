from typing import Optional
# Definition for a binary tree node
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def searchBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    while (root is not None and root.val != val):
        if (val < root.val):
            root = root.left
        else:
            root = root.right
    return root

if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    result = searchBST(root, 2)
    def Tree(node: Optional[TreeNode]) -> list:
        if not node:
            return []
        return [node.val] + Tree(node.left) + Tree(node.right)
    print(Tree(result))