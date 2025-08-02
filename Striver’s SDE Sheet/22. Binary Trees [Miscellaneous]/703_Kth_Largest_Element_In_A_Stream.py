import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minheap = nums
        heapq.heapify(self.minheap)
        while len(self.minheap) > k:
            heapq.heappop(self.minheap)
    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)
        if len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]

if __name__ == "__main__":
    kth_largest = KthLargest(3, [4, 5, 8, 2])
    print(kth_largest.add(3))  
    print(kth_largest.add(5))  
    print(kth_largest.add(10)) 
    print(kth_largest.add(9))  
    print(kth_largest.add(4))  