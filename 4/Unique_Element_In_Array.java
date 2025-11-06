public class Unique_Element_In_Array {
    public static int unique(int[] array) {
        int result = 0;
         
        for (int i = 0; i < array.length; i++) {
            result ^= array[i];
        }
        return result;
    }

    public static void main(String[] args) {
        int[] array = {5,3,2,3,2};
        System.out.println(unique(array));
    }
}