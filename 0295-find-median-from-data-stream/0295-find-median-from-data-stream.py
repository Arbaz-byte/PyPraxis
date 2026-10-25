class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        heappush(self.minHeap, -num)
        heappush(self.maxHeap, -heappop(self.minHeap))
        if len(self.maxHeap) > len(self.minHeap):
            heappush(self.minHeap, - heappop(self.maxHeap))

    def findMedian(self) -> float:
        return (self.minHeap[0] *(-1) + self.maxHeap[0])/2 if len(self.minHeap) == len(self.maxHeap) else self.minHeap[0] *(-1)



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()