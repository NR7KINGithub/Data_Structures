def BinarySearch(nums, target):
    n = len(nums)
    low, high = 0, n-1
    while low <= high:
        mid = (low+high)//2
        if(target == nums[mid]):
            return nums[mid]
        if(target > nums[mid]):
            low = mid+1
        if(target < nums[mid]):
            high = mid-1
    return False

def MatrixSearch(matrix, target):
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        if(matrix[i][0] <= target <= matrix[i][m-1]):
            return BinarySearch(matrix[i],target)
    return False

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
result = MatrixSearch(matrix, 8)
print("True" if result else "False")

"""// Java Solution
class Solution {
    public boolean binarySearch(int[] nums, int target) {
        int low = 0;
        int high = nums.length - 1;
        while (low <= high) {
            int mid = (low + high) / 2;
            if (nums[mid] == target) {
                return true;
            } else if (nums[mid] < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return false;
    }

    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix.length == 0 || matrix[0].length == 0) return false;
        int n = matrix.length;
        int m = matrix[0].length;
        for (int i = 0; i < n; i++) {
            if (matrix[i][0] <= target && target <= matrix[i][m - 1]) {
                if (binarySearch(matrix[i], target)) {
                    return true;
                }
            }
        }
        return false;
    }
}"""