class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:

        if len(nums) == 1:
            return nums
        if k >= len(nums):
            return [max(nums)]

        ans, dq = [], collections.deque()
        for r, num in enumerate(nums):
            while dq and nums[dq[-1]] < num:
                dq.pop()
            dq.append(r)

            if dq[0] <= r-k:
                dq.popleft()
            if r >= k-1:
                ans.append(nums[dq[0]])
        return ans


        