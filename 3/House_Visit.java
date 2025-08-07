public class House_Visit {
    public static int houseVisit(int N, int[] A) {
        int count = 0;
        int i = 1;
        
        while (i <= N) {
            count ++;
            i += A[i-1];
        }
        return count;
    }

    public static void main(String[] args) {
        int N = 4;
        int A[] = {2, 1, 3, 1};
        System.out.println(houseVisit(N, A));
    }
}