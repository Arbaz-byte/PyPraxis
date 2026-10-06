class NumArray:

    def __init__(self, nums: list[int]):
        self.prefixSum = []
        s = 0
        for n in nums:
            s += n
            self.prefixSum.append(s)

    def sumRange(self, left: int, right: int) -> int:
        rightSum = self.prefixSum[right]
        if left == 0:
            return rightSum
        leftSum = self.prefixSum[left-1]
        return rightSum - leftSum
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)