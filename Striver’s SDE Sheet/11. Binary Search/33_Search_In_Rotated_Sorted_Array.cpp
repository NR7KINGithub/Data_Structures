#include <bits/stdc++.h>
using namespace std;

int search(vector<int>& nums, int target) {
    int n = nums.size();
    int low = 0, high = n-1;
    while (low <= high) {
        int mid = (low+high)/2;
        // If mid points the target
        if (nums[mid] == target) return mid;
        // If the left part is sorted
        if (nums[low] <= nums[mid]) {
            if (nums[low] <= target && target <= nums[mid]) {
                // Element exists
                high = mid-1; }
            else {
                // Element does not exist
                low = mid+1;}
        }
        else { 
            // If right part is sorted
            if (nums[mid] <= target && target <= nums[high]) {
                // Element exists
                low = mid+1; }
            else {
                // Element does not exist
                high = mid-1; }
        }
    }
    return -1;
}
int main()
{
    vector<int> nums = {7, 8, 9, 1, 2, 3, 4, 5, 6};
    int target = 1;
    cout<<search(nums, target);
}