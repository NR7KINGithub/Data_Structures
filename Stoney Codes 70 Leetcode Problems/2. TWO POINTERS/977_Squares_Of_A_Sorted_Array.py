from typing import List

def sortedSquares(nums: List[int]) -> List[int]:
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    index = n - 1

    while left <= right:
        left_sq = nums[left] * nums[left]
        right_sq = nums[right] * nums[right]

        if left_sq > right_sq:
            result[index] = left_sq
            left += 1

        else:
            result[index] = right_sq
            right -= 1
        
        index -= 1

    return result

if __name__ == "__main__":
    nums = [-4,-1,0,3,10]
    print(sortedSquares(nums))

"""// Java Solution
class Solution {
    public int[] sortedSquares(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];
        int left = 0, right = n - 1, index = n - 1;

        while (left <= right) {
            int left_sq = nums[left] * nums[left];
            int right_sq = nums[right] * nums[right];

            if (left_sq > right_sq) {
                result[index] = left_sq;
                left += 1;
            }

            else {
                result[index] = right_sq;
                right -= 1;
            }
        
            index -= 1;
        }
    return result;
    }
}"""