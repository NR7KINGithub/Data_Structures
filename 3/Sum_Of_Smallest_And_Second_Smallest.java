public class Sum_Of_Smallest_And_Second_Smallest {
    public static int sum(int N, int[] A) {
        int smallest = Integer.MAX_VALUE;
        int second_smallest = Integer.MAX_VALUE;

        for (int num : A) {
            if (num <= smallest) {     
                second_smallest = smallest;
                smallest = num;
            } else if (num < second_smallest) {
                second_smallest = num;
            }
        }
        return smallest + second_smallest;
    }

    public static void main(String[] args) {
        int N = 3;
        int A[] = {3, 5, 1};
        System.out.println(sum(N, A));
    }
}