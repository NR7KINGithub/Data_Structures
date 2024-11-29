def merge(arr1, arr2, n, m):
    left = n-1
    right = 0

    while left >= 0 and right < m:
        if(arr1[left] > arr2[right]):
            arr1[left], arr2[right] = arr2[right], arr1[left]
            left -= 1
            right += 1
        else:
            break

    arr1.sort()
    arr2.sort()

arr1 = [1,4,8,10]
arr2 = [2,3,9]
n = 4
m = 3
merge(arr1, arr2, n, m)
print("The merged arrays are:")
print("arr1[] = ", end="")
for i in range(n):
    print(arr1[i], end=" ")
print("\narr2[] = ", end="")
for i in range(m):
    print(arr2[i], end=" ")
print()