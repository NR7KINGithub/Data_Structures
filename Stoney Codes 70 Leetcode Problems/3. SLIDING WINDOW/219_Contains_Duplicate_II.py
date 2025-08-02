from typing import List

def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    seen = set()

    for i, num in enumerate(nums):
        if num in seen:
            return True
        
        seen.add(num)

        if len(seen) > k:
            seen.remove(nums[i-k])

    return False

if __name__ == "__main__":
    nums = [1,2,3,1]
    k = 3
    print(containsNearbyDuplicate(nums, k))