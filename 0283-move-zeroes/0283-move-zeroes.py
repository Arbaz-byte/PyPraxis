class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0 # conunts number of zeros in the list
        for val in nums[:]:
            if val == 0:
                nums.remove(0)
                count+=1
        nums.extend([0] * count)