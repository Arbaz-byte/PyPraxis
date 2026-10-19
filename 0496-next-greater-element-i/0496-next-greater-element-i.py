class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:

        nums1Idx = {n:i for i, n in enumerate(nums1)} 
        result = [-1] * len(nums1)
        stack = []

        for i in range(len(nums2)):
            curr = nums2[i]
            while stack and curr > stack[-1]:
                val = stack.pop()
                indx = nums1Idx[val]
                result[indx] = curr
            if curr in nums1Idx:
                stack.append(curr)
        return result
        
        