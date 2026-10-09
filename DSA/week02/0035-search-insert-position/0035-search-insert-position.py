class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)-1
        found = False

        while left <= right:
            mid = left + (right - left) //2

            if nums[mid] == target:
                return mid
                found = True
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid -1 
        if not found:
            return left
             
        