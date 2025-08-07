public class Repeated_Sum_Of_Digits {
    public static int repeatedSumOfDigits(int N) {
        while (N / 10 > 0) {
            int sum = 0;
            
            while (N > 0) {
                sum += (N % 10);
                N /= 10; 
            }
            N = sum;
        }
        return N;
    }
    public static void main(String[] args) {
        int N = 38;
        System.out.println(repeatedSumOfDigits(N));
    }
}