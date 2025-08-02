class Solution():
    def largestSumCycle(self, N, Edge):
        visited = [False] * N
        max_cycle_sum = -1
        
        for start in range(N):
            if visited[start]:
                continue
            
            current_path = {}
            node = start
            step = 0
            
            while node != -1 and not visited[node]:
                if node in current_path:
                    cycle_sum = 0
                    cycle_start = node
                    curr = node
                    
                    while True:
                        cycle_sum += curr
                        curr = Edge[curr]
                        if curr == cycle_start:
                            break
                        
                    max_cycle_sum = max(max_cycle_sum, cycle_sum)
                    break
                
                current_path[node] = step
                step += 1
                
                node = Edge[node]
                
            for seen_node in current_path:
                visited[seen_node] = True

        return max_cycle_sum
    
N = 23
Edge = [4, 1, 4, 1, 3, 8, 8, 8, 0, 8, 14, 9, 15, 11, -1, 10, 15, 22, 22, 22, 22, 22, 21]
print(Solution().largestSumCycle(N, Edge))