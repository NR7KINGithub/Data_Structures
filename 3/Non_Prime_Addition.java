public class Non_Prime_Addition {
    public static int nonPrimeSumOfDigits(int num) {
        int count, digit, sum = 0;

        while (num > 0) {
            count = 0;
            digit  = num % 10;

            for (int i = 1; i <= digit; i++) {
                if (digit % i == 0) {
                    count++;
                }
            }
            
            if (count != 2) {
                sum += digit;
            }
            num /= 10;
        }
        return sum;
    }

    public static void main(String[] args) {
        int num = 597586;
        System.out.println(nonPrimeSumOfDigits(num));
    }
}