class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        result = []
        distance = [point[0]**2 + point[1]**2 for point in points]
        hq = distance.copy()
        heapq.heapify(hq)

        for i in range(k):
            thres = heapq.heappop(hq)

        for i in range(len(distance)):
            if distance[i] <= thres:
                result.append(points[i])

        return result


        


        

