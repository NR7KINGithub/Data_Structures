from typing import List

def moveZeroes(nums: List[int]) -> None:
    count = 0;
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[count] = nums[i]
            count += 1

    for i in range(count, len(nums)):
        nums[i] = 0

if __name__ == "__main__":
    print(moveZeroes([0,1,0,3,12]))
        


"""// Java Solution
class Solution {
    public void moveZeroes(int[] nums) {
        int count = 0;
        for (int i=0; i < nums.length; i++) {
            if (nums[i] != 0) {
                nums[count++] = nums[i];
            }
        }
        for (int i=count; i < nums.length; i++) {
            nums[i] = 0;
        }
    }
}"""