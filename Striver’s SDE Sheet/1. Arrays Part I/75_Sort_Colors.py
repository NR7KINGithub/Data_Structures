def sortArray(arr):
    cnt0 = 0
    cnt1 = 0
    cnt2 = 0

    for num in arr:
        if num == 0:
            cnt0 += 1
        elif num == 1:
            cnt1 += 1
        else:
            cnt2 += 1

    for i in range(cnt0):
        arr[i] = 0

    for i in range(cnt0, cnt0 + cnt1):
        arr[i] = 1

    for i in range(cnt0 + cnt1, len(arr)):
        arr[i] = 2

n = 6
arr = [0,2,1,2,0,1]
sortArray(arr)
print("After sorting:")
for num in arr:
    print(num, end=" ")
print()

"""// Java Solution
class Solution {
    public void sortColors(int[] nums) {
        int cnt0 = 0, cnt1 = 0, cnt2 = 0;
        
        for (int num : nums) {
            if (num == 0) cnt0++;
            else if (num == 1) cnt1++;
            else cnt2++;
        }
        
        int index = 0;
        for (int i = 0; i < cnt0; i++) nums[index++] = 0;
        for (int i = 0; i < cnt1; i++) nums[index++] = 1;
        for (int i = 0; i < cnt2; i++) nums[index++] = 2;
    }
}"""