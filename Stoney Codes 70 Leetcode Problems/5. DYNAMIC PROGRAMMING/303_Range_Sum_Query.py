from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = [0] * (len(nums)+1)

        for i, num in enumerate(nums):
            self.prefix_sum[i+1] = self.prefix_sum[i] + num

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right + 1] - self.prefix_sum[left]


if __name__ == "__main__":
    nums = [-2, 0, 3, -5, 2, -1]
    left = 0
    right = 2
    print(NumArray(nums).sumRange(left, right))