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

"""// Java Solution
class Solution {
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        // transposing the matrix
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
        // reversing each row of the matrix
        for (int i = 0; i < n; i++) {
            int left = 0;
            int right = n - 1;
            while(left < right) {
                int temp = matrix[i][left];
                matrix[i][left] = matrix[i][right];
                matrix[i][right] = temp;
                left++;
                right--;
            }
        }
    }
}"""

"""// Kotlin Solution
class Solution {
    fun rotate(matrix: Array<IntArray>): Unit {
         val n = matrix.size
        // transposing the matrix
        for (i in 0 until n) {
            for (j in i + 1 until n) {
                val temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
            }
        }
        // reversing each row of the matrix
        matrix.forEach { row -> row.reverse() }
    }
}"""