public class Printing_Job {
    public static int printJobs(int N, int X) {
        if (N <= 0 || X <= 0) {
            return 0;
        }

        return Math.max(0, ((N - 1)*10 - X*(N - 1)));
    }
    public static void main(String[] args) {
        int N = 4;
        int X = 5;
        System.out.println(printJobs(N, X));
    }
}