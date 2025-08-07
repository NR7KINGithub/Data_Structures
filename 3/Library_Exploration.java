public class Library_Exploration {
    public static int maxBooks(int N, int K, int[] A) {
        int count = 0;

        for (int i = 2; i <= N; i++) {
            int prime = 0;

            for (int j = 1; j <= i; j++) {
                if (i % j == 0) {
                    prime++;
                }
            }
            
            if (prime == 2) {
                if (A[i - 1] > K) {
                    count += K;
                }
                else {
                    count += A[i - 1];
                }
            }
        }
        return count;
    }

    public static void main(String[] args) {
        int N = 2;
        int K = 4;
        int A[] = {10, 2};
        System.out.println(maxBooks(N, K, A));
    }
}