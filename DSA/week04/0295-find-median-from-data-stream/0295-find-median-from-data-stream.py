class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:

        if not self.small or num <= -self.small[0]:
            heappush(self.small, -num)
            if len(self.small) > len(self.large) + 1 :
                heappush(self.large, -heappop(self.small))
        else:
            heappush(self.large, num)
            if len(self.large) > len(self.small):
                heappush(self.small, -heappop(self.large))


    def findMedian(self) -> float:

        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        else:
            return - self.small[0]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()