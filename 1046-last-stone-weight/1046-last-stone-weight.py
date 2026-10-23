class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        for i in range(len(stones)):
            stones[i] = -stones[i]
        
        heapq.heapify(stones)

        while stones:
            j = heapq.heappop(stones) * (-1)
            k = heapq.heappop(stones) * (-1) 

            if j > k:
                heapq.heappush(stones, (-1)*(j-k))

            if len(stones) == 1:
                break

        for i in range(len(stones)):
            stones[i] = -stones[i]
        
        if stones:
            return stones[0]
        else:
            return 0
