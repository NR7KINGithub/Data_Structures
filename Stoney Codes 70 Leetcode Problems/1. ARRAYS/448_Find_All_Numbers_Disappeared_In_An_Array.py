from typing import List

def findDisappearedNumbers(nums: List[int]) -> List[int]:
    nums_set = set(nums)
    result = []
    for num in range(1, len(nums)+1):
        if num not in nums_set:
            result.append(num)
    return result
    
if __name__ == "__main__":
    nums = [4,3,2,7,8,2,3,1]
    print(findDisappearedNumbers(nums))

"""// Java Solution
class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        Set<Integer> nums_set = new HashSet<>();
        List<Integer> result = new ArrayList<>();

        for (int num : nums) {
            nums_set.add(num);
        }

        for(int i = 1; i <= nums.length; i++) {
            if (!nums_set.contains(i)) {
                result.add(i);
            }
        }
        return result;
    }
}"""