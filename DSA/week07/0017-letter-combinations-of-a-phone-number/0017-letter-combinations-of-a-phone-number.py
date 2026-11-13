class Solution:
    def letterCombinations(self, digits: str) -> list[str]: 
        # Recursive Backtracking 

        if not digits:
            return []

        digit_map = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}

        result = []

        def backtrack(index:int, current_str:list[str]):
            # Hit the Base Case : append list elements to result
            if index == len(digits):
                result.append("".join(current_str))
                return

            # get digit and explor the paths 
            possible_latter = digit_map[digits[index]]
            for letter in possible_latter:
                current_str.append(letter)
                backtrack(index+1, current_str) # Call stack traverse using DFS
                current_str.pop() # Once leaves are done, back to privious
        backtrack(0, [])

        return result
    



      





