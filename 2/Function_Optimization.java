import java.util.Arrays;

public class Function_Optimization {
    public static int leastPossibleValue(int[] A, int N, int M) {
        Arrays.sort(A);
        int result = Integer.MAX_VALUE;
        for (int i = 0; i <= N-M; i++) {
            int curr_diff = A[i+M-1] - A[i];
            if (curr_diff < result) {
                result = curr_diff;
            }
        }
        return result;
    }

    public static void main(String[] args) {
        int[] A = { 3, 4, 3, 8, 1, 15, 20, 3 };
        int N = A.length;
        int M = 5;
        System.out.println(leastPossibleValue(A, N, M));
    }
}