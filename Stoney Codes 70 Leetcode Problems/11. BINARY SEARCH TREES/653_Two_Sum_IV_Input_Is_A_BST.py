from typing import Optional

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findTarget(root: Optional[Node], k: int) -> bool:
    nums = []
    # Inorder traversal to get sorted elements
    def inorder(node):
        if not node:
            return
        inorder(node.left)
        nums.append(node.val)
        inorder(node.right)
    inorder(root)
    
    # Two-pointer search
    left, right = 0, len(nums) - 1
    while left < right:
        s = nums[left] + nums[right]
        if s == k:
            return True
        elif s < k:
            left += 1
        else:
            right -= 1 
    return False
    
if __name__ == "__main__":
    root = Node(5)
    root.left = Node(3)
    root.right = Node(6)
    root.left.left = Node(2)
    root.left.right = Node(4)
    root.right.right = Node(7)
    print(findTarget(root, 9))