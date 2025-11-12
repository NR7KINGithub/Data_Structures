import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Sum_Of_Unique_Elements_1748 {
    public static int sumOfUnique(int[] nums) {
        Map<Integer, Integer> unique = new HashMap<>();

        for (int num : nums) {
            if (!unique.containsKey(num)) {
                unique.put(num, 1);
            }

            else {
                unique.put(num, unique.get(num) + 1);
            }
        }

        int sum = 0;
        for (int key : unique.keySet()) {
            if (unique.get(key) == 1) {
                sum += key;
            }
        }
        return sum;
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String[] str = scanner.nextLine().split(" ");
        int[] nums = new int[str.length];

        for (int i = 0; i < nums.length; i++) {
            nums[i] = Integer.parseInt(str[i]);
        }

        System.out.println(sumOfUnique(nums));
        scanner.close();
    }
}