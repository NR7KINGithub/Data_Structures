from typing import List

def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        start_color = image[sr][sc]
        
        if color == start_color:
            return image
        
        def dfs(i, j):
            if i < 0 or i >= m or  j < 0 \
                or j >= n or image[i][j] != start_color:
                return
            image[i][j] = color
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)
            
        dfs(sr, sc)
        return image

if __name__ == "__main__":
    print(floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))