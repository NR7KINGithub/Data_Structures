import heapq
def findKthLargest(nums, k):
        pq = []
        n = len(nums)
        for i in range(n):
            heapq.heappush(pq, -nums[i])
        f = k-1
        while f > 0:
            heapq.heappop(pq)
            f -= 1

        return -pq[0]

nums = [1,2,6,4,5,3]
print(findKthLargest(nums, 4))