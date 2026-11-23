class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        def max_rob(num: list[int]) -> int:
            prev, curr = num[0], max(num[0], num[1])

            for i in range(2,len(num)):
                prev, curr = curr, max(curr, prev + num[i])
            
            return curr
        
        return max(max_rob(nums[1:]), max_rob(nums[:-1]))