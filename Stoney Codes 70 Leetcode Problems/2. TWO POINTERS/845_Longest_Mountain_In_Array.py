from typing import List

def longestMountain(arr: List[int]) -> int:
    n = len(arr)
    max_len = 0
    i = 1
    
    while i < n - 1:
        isPeak = arr[i-1] < arr[i] > arr[i+1]
        if not isPeak:
            i += 1
            continue

        left = i - 1
        while left > 0 and arr[left] > arr[left-1]:
            left -= 1

        right = i + 1
        while right < n - 1 and arr[right] > arr[right+1]:
            right += 1

        curr_len = right - left + 1
        max_len = max(max_len, curr_len)

        i = right

    return max_len

if __name__ == "__main__":
    arr = [2,1,4,7,3,2,5]
    print(longestMountain(arr))

"""// Java Solution
class Solution {
    public int longestMountain(int[] arr) {
        int n = arr.length;
        int max_len = 0;
        int i = 1;
        
        while (i < n - 1) {
            boolean isPeak = arr[i-1] < arr[i] && arr[i] > arr[i+1];
            if (!isPeak) {
                i += 1;
                continue;
            }

            int left = i - 1;
            while (left > 0 && arr[left] > arr[left-1]) {
                left -= 1;
            }

            int right = i + 1;
            while (right < n - 1 && arr[right] > arr[right+1]) {
                right += 1;
            }

            int curr_len = right - left + 1;
            max_len = Math.max(max_len, curr_len);

            i = right;
        }
        return max_len;
    }
}"""