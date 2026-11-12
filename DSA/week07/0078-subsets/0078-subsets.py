class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:

        subset = [[]]
        for num in nums:
            new_sub = [[num] + curr for curr in subset]
            subset.extend(new_sub)
        
        return subset
