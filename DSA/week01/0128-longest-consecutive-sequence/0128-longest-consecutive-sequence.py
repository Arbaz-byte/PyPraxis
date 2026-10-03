class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = list(set(nums))
        nums = sorted(nums)

        count = 1
        output=[]

        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                count +=1
            else:
                output.append(count)
                count = 1
        if count != 1 or len(nums)==1:
            output.append(count)
        if output == []:
            return 0
        else:
            return max(output)
