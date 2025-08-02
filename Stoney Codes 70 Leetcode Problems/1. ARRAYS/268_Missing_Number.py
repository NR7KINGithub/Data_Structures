from typing import List

def missingNumber(nums: List[int]) -> int:
    n = len(nums)
    expectedSum = n * (n+1) // 2
    actualSum = 0
    for num in nums:
        actualSum += num
    return expectedSum - actualSum

if __name__ == "__main__":
    nums = [9,6,4,2,3,5,7,0,1]
    print(missingNumber(nums))

"""// Java Solution
class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int expectedSum = n * (n+1) / 2;
        int actualSum = 0;
        for (int num : nums) {
            actualSum += num;
        }
    return expectedSum - actualSum;
    }
}"""