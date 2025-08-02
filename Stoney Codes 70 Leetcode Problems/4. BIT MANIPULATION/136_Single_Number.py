from typing import List

def singleNumber(nums: List[int]) -> int:
    xor = 0
    for num in nums:
        xor ^= num

    return xor

if __name__ == "__main__":
    nums = [4,1,2,1,2]
    print(singleNumber(nums))

"""// Java Solution
class Solution {
    public int singleNumber(int[] nums) {
        int xor = 0;
        for (int i = 0; i < nums.length; i++) {
            xor ^= nums[i];
        }
        return xor;
    }
}"""