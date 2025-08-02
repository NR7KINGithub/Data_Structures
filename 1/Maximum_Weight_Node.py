class Solution():
    def maxWeightCell(self, exits):
        n = len(exits)
        weight = [0] * n
        
        for j, exit in enumerate(exits):
            if exit != -1:
                weight[exit] += j

        max_weight = -1
        ans = -1
        for i in range(n):
            if weight[i] > max_weight or (weight[i] == max_weight and i > ans):
                max_weight = weight[i]
                ans = i

        return ans
    
exits = [4, 1, 4, 1, 3, 8, 8, 8, 0, 8, 14, 9, 15, 11, -1, 10, 15, 22, 22, 22, 22, 22, 21]
print(Solution().maxWeightCell(exits))