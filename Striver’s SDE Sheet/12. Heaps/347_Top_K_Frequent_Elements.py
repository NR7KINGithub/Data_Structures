import heapq
from collections import Counter

def topKFrequent(nums, k):
    counter = Counter(nums)
    heap = []
    
    for num, freq in counter.items():
        heapq.heappush(heap, (-freq, num))
    
    result = []
    for _ in range(k):
        result.append(heapq.heappop(heap)[1])
    return result

nums = [1,1,1,2,2,3]
print(topKFrequent(nums, 2))