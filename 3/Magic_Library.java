public class Magic_Library {
    public static int magicalRows(int M, int N, int[][] A) {
        int count = 0;

        for (int i = 0; i < M; i++) {
            int oddSum = 0;

            for (int j = 0; j < N; j++) {
                if (A[i][j] % 2 != 0) {
                    oddSum += A[i][j];
                }
            }
            
            if (oddSum % 2 == 0) {
                count++;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        int M = 3;
        int N = 3;
        int A[][] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        System.out.println(magicalRows(M, N, A));
    }
}