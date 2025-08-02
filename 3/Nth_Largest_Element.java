import java.util.Arrays;

public class Nth_Largest_Element {
    public static int nthLargest(int[] a, int n, int k) {
        Arrays.sort(a);
        return a[n-k];
    }

    public static void main(String[] args) {
        int n = 5;
        int k = 3;
        int[] a = { 11, -1, -4, 12, -6 };
        System.out.println(nthLargest(a, n, k));
    }
}