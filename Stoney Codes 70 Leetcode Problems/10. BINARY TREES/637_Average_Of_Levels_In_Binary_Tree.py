from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def averageOfLevels(root: Optional[TreeNode]) -> List[float]:
    queue = deque([root])
    result = []

    while queue:
        level= []
        for i in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)

            if node.left:   queue.append(node.left)
            if node.right:  queue.append(node.right)

        result.append(sum(level) / len(level))

    return result

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(averageOfLevels(root))