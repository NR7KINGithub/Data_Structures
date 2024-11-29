def uniquePaths(m: int, n: int) -> int:
    grid = []
    for i in range(m):
        grid.append([0] * n)
        
    grid[0][0] = 1
    
    for i in range(m):
        for j in range(n):
            if (i == 0 and j == 0):
                continue
            elif i == 0:
                grid[i][j] = grid[i][j-1]
            else:
                grid[i][j] = grid[i][j-1] + grid[i-1][j]
                
    return grid[-1][-1]

if __name__ == "__main__":
    print(uniquePaths(3, 7))