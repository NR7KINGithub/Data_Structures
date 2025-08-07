import java.util.Arrays;

public class Duplicate_Array {
    public static int[] duplicateArray(int A[], int N) {
        int result[] = new int [N*2];
        
        for (int i = 0; i < N; i++) {
            result[i] = A[i];
        }
        for (int i = 0; i < N; i++) {
            result[N+i] = A[i];
        }
        return result;
    }
    public static void main(String[] args) {
        int A[] = {1, 2, 3};
        int N = 3;
        System.out.println(Arrays.toString(duplicateArray(A, N)));
    }
}