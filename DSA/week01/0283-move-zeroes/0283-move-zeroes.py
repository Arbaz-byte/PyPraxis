class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        non_zero = []
        count=0
        for num in nums:
            if num != 0:
                non_zero.append(num)
            else:
                count+=1
        non_zero.extend([0] * count)
        
        for i in range(len(non_zero)):
            nums[i]=non_zero[i]
     

        
