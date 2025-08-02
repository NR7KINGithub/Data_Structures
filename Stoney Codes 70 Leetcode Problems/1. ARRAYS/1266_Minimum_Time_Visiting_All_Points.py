from typing import List

def minTimeToVisitAllPoints(points: List[List[int]]) -> int:
    result = 0
    x1, y1 = points.pop()

    while points:
        x2, y2 = points.pop()
        result += max(abs(y2 - y1), abs(x2 - x1))
        x1, y1 = x2, y2
    
    return result

if __name__ == "__main__":
    points = [[1,1],[3,4],[-1,0]]
    print(minTimeToVisitAllPoints(points))