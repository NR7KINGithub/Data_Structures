class Insertion_Sort {
    public static int[] sortArray(int[] nums) {
        int n = nums.length;
        for (int i = 0; i <= n-1; i++) {
            int j = i;
            while (j > 0 && nums[j-1] > nums[j]) {
                int temp = nums[j-1];
                nums[j-1] = nums[j];
                nums[j] = temp;
                j--;
            }
        }
        return nums;
    }

    public static void main(String args[]) {
        int nums[] = {5,1,1,2,0,0};
        System.out.println("Before Insertion Sort:");
        for (int i = 0; i < nums.length; i++) {
            System.out.print(nums[i] + " ");
        }
        System.out.println();

        sortArray(nums);
        
        System.out.println("After Insertion Sort:");
        for (int i = 0; i < nums.length; i++) {
            System.out.print(nums[i] + " ");
        }
        System.out.println();
    }
}

// Time Complexity:
// Best Case: O(n)
// Average & Worst Case: O(n^2)