from typing import List

def secondLargest(nums: List[int]) -> int:
    largest = float('-inf')
    second_largest = float('-inf')

    for i in range(len(nums)):
        if nums[i] > largest:
            largest = nums[i]

    for i in range(len(nums)):
        if nums[i] > second_largest and nums[i] != largest:
            second_largest = nums[i]

    return second_largest

if __name__ == "__main__":
    nums = [1, 2, 4, 7, 7, 5]
    print(secondLargest(nums))