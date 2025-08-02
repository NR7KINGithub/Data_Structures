public class Flipkart_Virus {
    public static int sumOfLastThree(int N) {
        int N1 = 0, N2 = 0, N3 = 1;
        int N4 = 1;
        if (N <= 0) {
            return -1;
        }
        else if (N == 1) {
            return N1;
        }
        else if (N == 2) {
            return N2;
        }
        else if (N == 3) {
            return N3;
        }
        else {
            for (int i = 4; i <= N; i++) {
                N4 = N1 + N2 + N3;
                N1 = N2;
                N2 = N3;
                N3 = N4;
            }
        }
        return N4;
    }

    public static void main(String[] args) {
        int N = 11;
        System.out.println(sumOfLastThree(N));
    }
}