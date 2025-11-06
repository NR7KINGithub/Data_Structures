public class Kaprekar_Number {
    public static boolean isKaprekar(int n) {
        if (n == 1) {
            return true;
        }

        int sq = n * n;
        int temp = sq;
        int digits = 0;

        while (temp != 0) {
            digits++;
            temp /= 10;
        }

        for (int i = 1; i < digits; i++) {
            int split = (int) Math.pow(10, i);

            if (split == n) {
                continue;
            }

            int sum = (sq / split) + (sq % split);
            if (sum == n) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        int n = 297;
        System.out.println(isKaprekar(n));
    }
}