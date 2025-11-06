class Sum_Of_Range {
    public static int sum(int[] range) {
        int m = range[0];
        int n = range[1];
        int sum = 0;

        while (m <= n) {
            sum += m;
            m++;
        }
        return sum;
    }

    public static void main(String[] args) {
        int[] range = {0,3};
        System.out.println(sum(range));
    }
}