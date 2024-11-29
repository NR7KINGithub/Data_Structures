from typing import List

def rotate(matrix: List[List[int]]) -> None:
    n = len(matrix)
    # transposing the matrix
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # reversing each row of the matrix
    for i in range(n):
        matrix[i].reverse()

arr = [[1,2,3], [4,5,6], [7,8,9]]
rotate(arr)
print("Rotated Image")
for i in range(len(arr)):
    for j in range(len(arr[0])):
        print(arr[i][j], end=" ")
    print()