class Solution:
    def singleNonDuplicate(self, nums):
        n = len(nums)
        # Edge cases
        if (n == 1):
            return nums[0]
        if (nums[0] != nums[1]):
            return nums[0]
        if (nums[n-1] != nums[n-2]):
            return nums[n-1]

        low = 1
        high = n-2
        while (low <= high):
            mid = (low+high)//2
            # If arr[mid] is the single element
            if (nums[mid] != nums[mid+1] and nums[mid] != nums[mid-1]):
                return nums[mid]
            # If single element is in the left
            if (mid%2==1 and nums[mid]==nums[mid-1])or(mid%2==0 and nums[mid]==nums[mid+1]):
            # Eliminate the left half
                low = mid+1
            # If single element is in the right
            else:
            # Eliminate the right half
                high = mid-1
        return -1

if __name__ == "__main__":
    s = Solution()
    print(s.singleNonDuplicate([1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]))