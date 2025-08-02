from typing import List, Optional

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[Node]:
        if not nums:
            return None

        mid = len(nums) // 2
        
        root = Node(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root
    
if __name__ == "__main__":
    print(Solution().sortedArrayToBST([-10, -3, 0, 5, 9]))