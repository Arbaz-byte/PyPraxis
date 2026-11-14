class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:

        result = []
        def backtrack(index:int, current:list[int], remaining:int):

            # Base Cases:
            if remaining == 0:
                result.append(current.copy())
                return
            if remaining < 0 or index >= len(candidates):
                return
            
            # Choice 1: Explore the candidates[index] (untill hit the base case then retrun)
            current.append(candidates[index])
            backtrack(index, current, remaining - candidates[index])

            # Hit the base case , undo (backtrack)
            current.pop()

            # Choice 2: Explore the candidates[index+1]
            backtrack(index + 1, current, remaining)
        
        backtrack(0, [], target)
        return result
    

        