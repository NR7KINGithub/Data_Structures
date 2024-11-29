from typing import List

def LongestSubarray(arr: List[int]) -> int:
    maxi = 0
    for i in range(len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]
            if sum == 0:
                maxi = max(maxi, j-i+1)
    return maxi
arr = [9, -3, 3, -1, 6, -5]
print(LongestSubarray(arr))