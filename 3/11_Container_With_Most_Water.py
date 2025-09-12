from typing import List

def maxArea(height: List[int]) -> int:
    l, r = 0, len(height) - 1
    maxi = 0

    while l < r:
        h = min(height[l], height[r])
        area = h * (r - l)
        
        if area > maxi:
            maxi = area
        
        if height[l] < height[r]:
            l += 1
        
        else:
            r -= 1
    return maxi

if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    print(maxArea(height))

"""// Java Solution
class Solution {
    public int maxArea(int[] height) {
        int l = 0, r = height.length - 1, maxi = 0;

        while (l < r) {
            int h = Math.min(height[l], height[r]);
            int area = h * (r - l);
            
            if (area > maxi) {
                maxi = area;
            }
            
            if (height[l] < height[r]) {
                l++;
            }
            else {
                r--;
            }
        }
        return maxi;
    }
}"""