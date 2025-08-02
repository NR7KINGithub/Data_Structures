from typing import List

def trap(height: List[int]) -> int:
        left_wall = right_wall = 0
        n = len(height)
        max_left = [0]*n
        max_right = [0]*n
        
        for i in range(n):
            j = -i - 1
            max_left[i] = left_wall
            max_right[j] = right_wall
            left_wall = max(left_wall, height[i])
            right_wall = max(right_wall, height[j])
            
        result = 0
        for i in range(n):
            potential = min(max_left[i], max_right[i])
            result += max(0, potential - height[i])
            
        return result
    #Time Complexity: O(n)
    #Space Complexity: O(n)

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))