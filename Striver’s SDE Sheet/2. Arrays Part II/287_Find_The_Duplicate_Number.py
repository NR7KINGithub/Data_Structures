def findDuplicate(arr):
    n = len(arr)
    arr.sort()
    for i in range(n):
        if (arr[i] == arr[i+1]):
            return arr[i]
        
arr = [1,3,4,2,2]
print(findDuplicate(arr))

"""// Java Solution
class Solution {
    public int findDuplicate(int[] nums) {
        // Find the intersection point in the cycle
        int slow = nums[0];
        int fast = nums[0];
        do {
            slow = nums[slow];
            fast = nums[nums[fast]];
        } while (slow != fast);

        // Find the entrance to the cycle
        slow = nums[0];
        while (slow != fast) {
            slow = nums[slow];
            fast = nums[fast];
        }
        return slow;
    }
}"""