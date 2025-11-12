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

"""// Java Solution
class Solution {
    public static int count(int[] nums) {
        int maxi = Integer.MIN_VALUE;        
        int count = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > maxi) {
                maxi = nums[i];
                count ++;
            }
        }
        return count;
    }
    
    public static void main(String[] args) {
        int[] nums = {7, 4, 8, 2, 9};
        System.out.println(count(nums));   
    }
}"""