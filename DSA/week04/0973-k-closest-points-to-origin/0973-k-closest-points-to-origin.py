class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:

        heap = []
        for point in points:
            x,y = point
            distance = x**2 + y**2
            heapq.heappush(heap, (distance, point))
        
        ans = [heapq.heappop(heap)[1] for _ in range(min(k, len(heap)))]
        return ans



        


        

