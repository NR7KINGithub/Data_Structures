from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    return (len(set(nums)) != len(nums))

if __name__ == "__main__":
    nums = [1,2,3,1]
    print(containsDuplicate(nums))

"""// Java Solution
class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> set = new HashSet<>();

        for (int num : nums) {
            set.add(num);
        }

        return set.size() != nums.length;
    }
}
"""