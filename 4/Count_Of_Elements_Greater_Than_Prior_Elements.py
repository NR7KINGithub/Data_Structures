from typing import List

def count(nums: List[int]) -> int:
    maxi = float('-inf')
    count = 0
    for i in range(len(nums)):
        if (nums[i] > maxi):
            maxi = nums[i]
            count += 1
    return count

if __name__ == "__main__":
    nums = [7,4,8,2,9]
    print(count(nums))