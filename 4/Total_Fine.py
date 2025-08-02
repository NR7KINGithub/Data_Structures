from typing import List

def fine(nums: List[int], d: int, x: int) -> int:
    count = 0

    if d % 2 == 0:
        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                count += 1
    else:
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                count += 1

    return count * x

if __name__ == "__main__":
    nums = [5,2,3,7]
    d = 12
    x = 200
    print(fine(nums, d, x))