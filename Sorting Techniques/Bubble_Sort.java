class Bubble_Sort {
    public static int[] sortArray(int[] nums) {
        int n = nums.length;
        for (int i = 0; i < n-1; i++) {
            boolean swap = false;
            for (int j = 0; j < n-1; j++) {
                if (nums[j] > nums[j+1]) {
                    int temp = nums[j];
                    nums[j] = nums[j+1];
                    nums[j+1] = temp;
                    swap = true;
                }
            }
            if (!swap) { break; } 
        }
        return nums;
    }

    public static void main(String args[]) {
        int nums[] = {5,1,1,2,0,0};
        System.out.println("Before Bubble Sort:");
        for (int i = 0; i < nums.length; i++) {
            System.out.print(nums[i] + " ");
        }
        System.out.println();

        sortArray(nums);
        
        System.out.println("After Bubble Sort:");
        for (int i = 0; i < nums.length; i++) {
            System.out.print(nums[i] + " ");
        }
        System.out.println();
    }
}

// Time Complexity:
// Best Case: O(n)
// Average & Worst Case: O(n^2)