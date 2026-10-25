class MedianFinder:

    def __init__(self):
        self.sorted = []
        

    def addNum(self, num: int) -> None:
        bisect.insort(self.sorted, num)
    
    def findMedian(self) -> float:
        if len(self.sorted) % 2 != 0:
            return self.sorted[len(self.sorted) // 2]
        else:
            i = len(self.sorted) //2 - 1 
            j = len(self.sorted) // 2

            return (self.sorted[i] + self.sorted[j]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()