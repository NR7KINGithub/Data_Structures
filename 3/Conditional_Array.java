public class Conditional_Array {
    public static void marks(int n, int array[]) {
        for (int i = 0; i < array.length; i++) {

            if (array[i] >= 81 && array[i] <= 100) {
                System.out.print("S ");
            }
            else if (array[i] >= 61 && array[i] <= 80) {
                System.out.print("A ");
            }
            else if (array[i] >= 51 && array[i] <= 60) {
                System.out.print("B ");
            }
            else if (array[i] >= 41 && array[i] <= 50) {
                System.out.print("C ");
            }
            else if (array[i] >= 10 && array[i] <= 40) {
                System.out.print("F ");
            }
            else  {
                System.out.print("Invalid ");
            }
        }
    }

    public static void main(String[] args) {
        int n = 5;
        int[] array = {81, 61, 51, 41, 11};
        marks(n, array);
    }
}