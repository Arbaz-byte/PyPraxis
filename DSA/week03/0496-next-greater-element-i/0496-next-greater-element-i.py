class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:

        nums1Idx = {n:i for i, n in enumerate(nums1)} 
        result = [-1] * len(nums1)

        for j in range(len(nums2)):
            if nums2[j] not in nums1Idx :
                continue
            for i in range(j+1, len(nums2)):
                if nums2[i] > nums2[j]:
                    idx = nums1Idx[nums2[j]]
                    result[idx] = nums2[i]
                    break
        return result 