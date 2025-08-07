import java.util.Arrays;

public class Knowledge_Enhancement {
    public static int readingBooks(int[] A, int N, int n) {
        Arrays.sort(A);
        int hours = 0, count  = 0;

        for (int i = 0; i < n; i++) {
            if (hours + A[i] <= N) {
                count += 1;
                hours += A[i];
            } 
        }
        return count;
    }

    public static void main(String[] args) {
        int A[] = {4, 2, 3, 1};
        int N = 5;
        int n = 4;
        System.out.println(readingBooks(A, N, n));
    }
}
