class Selection_Sort {
    public static int[] sortArray(int[] nums) {
        int n = nums.length;
        for (int i = 0; i < n-1; i++) {
            int min = i;
            for (int j = i+1; j < n; j++) {
                if (nums[j] < nums[min]) {
                    min = j;
                }
            }
            int temp = nums[min];
            nums[min] = nums[i];
            nums[i] = temp;
        }
        return nums;
    }

    public static void main(String args[]) {
        int nums[] = {5,1,1,2,0,0};
        System.out.println("Before Selection Sort:");
        for (int i = 0; i < nums.length; i++) {
            System.out.print(nums[i] + " ");
        }
        System.out.println();

        sortArray(nums);
        
        System.out.println("After Selection Sort:");
        for (int i = 0; i < nums.length; i++) {
            System.out.print(nums[i] + " ");
        }
        System.out.println();
    }
}

// Time Complexity:
// Best, Average & Worst Case: O(n^2)