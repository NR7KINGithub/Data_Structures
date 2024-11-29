def findDuplicate(arr):
    n = len(arr)
    arr.sort()
    for i in range(n):
        if (arr[i] == arr[i+1]):
            return arr[i]
        
arr = [1,3,4,2,2]
print(findDuplicate(arr))