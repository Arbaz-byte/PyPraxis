class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        
        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)

        while len(stones) > 1:
            j = heapq.heappop(stones) * (-1)
            k = heapq.heappop(stones) * (-1) 

            if (j - k)>0:
                heapq.heappush(stones, (-1)*(j-k))

        return -stones[0] if stones else 0

