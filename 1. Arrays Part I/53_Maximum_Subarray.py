from typing import List

def maxSubArray(nums: List[int]) -> int:
    max_sum = float('-inf')
    cur_sum = 0
    n = len(nums)
    
    for i in range(n):
        cur_sum += nums[i]
        max_sum = max(max_sum, cur_sum)
        if cur_sum < 0:
            cur_sum = 0
    return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))