from typing import List

def maxSubArray(nums: List[int]) -> int:
    dp = [0] * len(nums)

    for i, n in enumerate(nums):
        dp[i] = max(n, dp[i-1]+n)

    return max(dp)

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))