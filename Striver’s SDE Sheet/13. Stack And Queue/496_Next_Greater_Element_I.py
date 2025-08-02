from typing import List

def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    next_greater = {}
    stack = []
    for num  in nums2:
        while stack and stack[-1] < num:
            next_greater[stack.pop()] = num
        stack.append(num)
    while stack:
        next_greater[stack.pop()] = -1
    return [next_greater[num] for num in nums1]   

if __name__ == "__main__":
    print(nextGreaterElement([4,1,2], [1,3,4,2]))