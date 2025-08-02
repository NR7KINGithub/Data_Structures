from typing import List

def smallerNumbersThanCurrent(nums: List[int]) -> List[int]:
    temp =sorted(nums)
    d = {}
    result = []

    for i, num in enumerate(temp):
        if num not in d:
            d[num] = i

    for i in nums:
        result.append(d[i])
    
    return result

if __name__ == "__main__":
    nums = [8,1,2,2,3]
    print(smallerNumbersThanCurrent(nums))

"""// Java Solution
class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        int[] temp = nums.clone();
        Arrays.sort(temp);
        Map<Integer, Integer> map = new HashMap<>();
        int[] result = new int[nums.length];

        for (int i = 0; i < temp.length; i++) {
            if (!map.containsKey(temp[i])) {
                map.put(temp[i], i);
            }
        }

        for (int i = 0; i < nums.length; i++) {
            result[i] = map.get(nums[i]);
        }

        return result;
    }
}"""