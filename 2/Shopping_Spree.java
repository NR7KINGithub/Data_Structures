public class Shopping_Spree {
    public static int knapsack(int n, int capacity, int[] profits, int[] weights) {
        int[] dp = new int[capacity + 1];
        for (int i = 1; i <= weights.length; i++) {
            for (int j = capacity; j >= weights[i - 1]; j--) {
                dp[j] = Math.max(dp[j], dp[j - weights[i - 1]] + profits[i - 1]);
            }
        }
        return dp[capacity];
    }

    public static void main(String[] args) {
        int n = 4;
        int capacity = 4;
        int[] profits= {5, 3, 2, 4};
        int[] weights = {4, 5, 1, 3};
        System.out.println(knapsack(n, capacity, profits, weights));
    }
}