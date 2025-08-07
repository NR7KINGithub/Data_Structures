public class Red_Pen_Green_Pen {
    public static int switchCount(int N, int[] A) {
        int count = 0;
        
        for (int i = 0; i < N-1; i++) {
            if (A[i] % 2 != 0 && A[i+1] % 2 == 0) {
                count++;
            } 
        }
        return count;
    }
    public static void main(String[] args) {
        int N = 6;
        int A[] = {70, 23, 13, 26, 72, 19};
        System.out.println(switchCount(N, A));
    }
}