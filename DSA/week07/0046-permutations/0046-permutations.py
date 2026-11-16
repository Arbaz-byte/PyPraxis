class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:

        result = []
        used = [False]*len(nums)
        def backtrack(path:list[int]):

            # Base Case : Current permulation is complete
            if len(path) == len(nums):
                result.append(path.copy())
                return
            
            for i in range(len(nums)):
                # Skip element already in path
                if used[i]:
                    continue
                
                # chose the element 
                used[i] = True
                path.append(nums[i])

                # Explore further
                backtrack(path)

                # Backtrack : Undo choice 
                path.pop()
                used[i] = False
            
        backtrack([])
        return result

            


        