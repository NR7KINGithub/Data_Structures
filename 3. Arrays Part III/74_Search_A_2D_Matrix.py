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