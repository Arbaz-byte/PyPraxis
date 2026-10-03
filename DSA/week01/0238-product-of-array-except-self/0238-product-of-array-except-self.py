class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        output = [1]*len(nums)
        for i in range(1,len(nums)):
            output[i] = nums[i-1]*output[i-1]

        postfix = 1
        for i in range(len(nums)-1,-1, -1):
            output[i] = postfix * output[i]
            postfix *= nums[i]

        return output


