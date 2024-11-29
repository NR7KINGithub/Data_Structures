class Solution:
    def TwoSum(self, arr: list[int], target: int) -> list[int]:
        left, right = 0, len(arr) - 1
        while (left < right):
            sum = arr[left] + arr[right]
            if (sum == target):
                return [left, right]
            elif (sum < target):
                left += 1
            else:
                right -= 1

if __name__ == "__main__":
    s = Solution()
    print(s.TwoSum([2,7,11,15], 9))