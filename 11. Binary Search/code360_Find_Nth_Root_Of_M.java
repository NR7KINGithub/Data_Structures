public class code360_Find_Nth_Root_Of_M {
    public static int NthRoot(int n, int m) {
        if(m == 1) {
            return 1;
        }
        int left = 1, right = m;

        while (left <= right) {
            int mid = 0;
            double power = 0.0d;
            mid = (left + right) / 2;
            power = Math.pow(mid, n);
            
            if(power == m)
                return mid;
            else if(power < m)
                left = mid + 1;
            else
                right = mid - 1;
        }
    return -1;
    }
    public static void main(String[] args) {
        System.out.println(NthRoot(3, 27));
    }
}