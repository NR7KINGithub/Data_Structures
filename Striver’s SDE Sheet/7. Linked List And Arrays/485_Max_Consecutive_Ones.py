def findMaxConsecutiveOnes(nums):
    cnt = 0
    maxi = 0
    for i in range(len(nums)):
        if(nums[i] == 1):
            cnt +=1
        else:
            cnt = 0
        maxi = max(cnt, maxi)
    return maxi

nums = [1, 0, 1, 1, 1, 1]
print(findMaxConsecutiveOnes(nums))

"""// Java Solution
class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int cnt = 0;
        int maxi = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) {
                cnt += 1;
            }
            else {
                cnt = 0;
            }
            maxi = Math.max(maxi, cnt);
        }
        return maxi;
    }
}"""