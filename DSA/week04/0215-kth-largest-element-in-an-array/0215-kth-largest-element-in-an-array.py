class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        ans = 0 
        while k > 0:
            ans = heapq.heappop(nums)
            k-=1
        
        return -ans