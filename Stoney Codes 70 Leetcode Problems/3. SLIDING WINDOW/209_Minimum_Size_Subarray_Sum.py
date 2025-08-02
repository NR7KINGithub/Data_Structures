from typing import List

def minSubArrayLen(target: int, nums: List[int]) -> int:
    n = len(nums)
    left = 0
    curr_sum = 0
    min_length = float('inf')

    for right in range(n):
        curr_sum += nums[right]

        while curr_sum >= target:
            min_length = min(min_length, right - left + 1)
            curr_sum -= nums[left]
            left += 1

    return min_length if min_length != float('inf') else 0

if __name__ == "__main__":
    nums = [2,3,1,2,4,3]
    target = 7
    print(minSubArrayLen(target, nums))

"""// Java Solution
class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int n = nums.length;
        int left = 0;
        int curr_sum = 0;
        int min_length = Integer.MAX_VALUE;

        for (int right = 0; right < n; right++) {
            curr_sum += nums[right];

            while (curr_sum >= target) {
                min_length = Math.min(min_length, right - left + 1);
                curr_sum -= nums[left];
                left +=1;
            }
        }
        return min_length == Integer.MAX_VALUE ? 0 : min_length;
    }
}"""