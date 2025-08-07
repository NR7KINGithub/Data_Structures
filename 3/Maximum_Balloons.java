public class Maximum_Balloons {
    public static int maxBalloons(int N, int X, int[] A, int[] B) {
        int max_balloons = 0;

        for (int i = 0; i < N; i++) {

            for (int j = i+1; j < N; j++) {
                int total_cost = B[i] + B[j];
                
                if (total_cost <= X) {
                    int total_balloons = A[i] + A[j];
                    max_balloons = Math.max(max_balloons, total_balloons);
                }
            }
        }
        return max_balloons;
    }

    public static void main(String[] args) {
        int N = 4;
        int X = 8;
        int A[] = {4, 6, 2, 7};
        int B[] = {5, 3, 1, 6};
        System.out.println(maxBalloons(N, X, A, B));
    }
}