import java.util.Scanner;

public class Maximum_Subarray {
    public static int maxSubArray(int[] nums) {
        int dp[] = new int[nums.length];

        for (int i = 0; i < nums.length; i++) {
            if (i == 0) {
                dp[i] = nums[i];
            } else {
                dp[i] = Math.max(nums[i], dp[i - 1] + nums[i]);
            }
        }

        int max = Integer.MIN_VALUE;
        for (int value : dp) {
            if (value > max) {
                max = Math.max(max, value);
            }
        }
        return max;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String[] str = scanner.nextLine().split(" ");
        int[] nums = new int[str.length];

        for (int i = 0; i < nums.length; i++) {
            nums[i] = Integer.parseInt(str[i]);
        }

        System.out.println(maxSubArray(nums));
        scanner.close();
    }
}