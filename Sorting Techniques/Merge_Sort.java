// Merge Sort
class Merge_Sort {
    public static int[] sortArray(int[] nums) {
        int n = nums.length;
        // Base case: an array of 0 or 1 element is already sorted
        if (n <= 1) {
            return nums;
        }
         // Find the middle index and split the array into two halves
        int mid = n / 2;
        int[] left = new int [mid];
        int[] right = new int [n-mid];
        // Copy elements into the left and right arrays
        for (int i = 0; i < mid; i++) {
            left[i] = nums[i];
        }
        // Recursively sort both halves
        for (int i = mid; i < n; i++) {
            right[i-mid] = nums[i];
        }
        // Merge the sorted halves and return the merged array
        left = sortArray(left);
        right = sortArray(right);
        // Merge the sorted halves and return the merged array
        return merge(left, right);
    }
    // Merge function to combine two sorted arrays into one sorted array
    private static int[] merge(int[] left, int[] right) {
        int[] merged = new int[left.length + right.length];
        int i = 0; // Pointer for left array
        int j = 0; // Pointer for right array
        int k = 0; // Pointer for merged array

        // Merge both arrays while elements remain in each array
        while (i < left.length && j < right.length) {
            if (left[i] <= right[j]) {
                merged[k++] = left[i++];
            } else {
                merged[k++] = right[j++];
            }
        }
        // Copy any remaining elements from the left array
        while (i < left.length) {
            merged[k++] = left[i++];
        }
        // Copy any remaining elements from the right array
        while (j < right.length) {
            merged[k++] = right[j++];
        }
        return merged;
    }
    
    public static void main(String[] args) {
        int nums[] = {5, 1, 1, 2, 0, 0};
        System.out.println("Before Merge Sort:");
        for (int num : nums) {
            System.out.print(num + " ");
        }
        System.out.println();

        nums = sortArray(nums);

        System.out.println("After Merge Sort:");
        for (int num : nums) {
            System.out.print(num + " ");
        }
        System.out.println();
    }
}