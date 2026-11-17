class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        result, sol = [], []
        def backtrack(open_count:int = 0, close_count:int = 0) ->list[str]:
            # Base Case : 
            if len(sol) == 2*n:
                result.append("".join(sol))
                return

            # Track Left : Open parenthese
            if open_count < n:
                sol.append('(')
                backtrack(open_count + 1, close_count)
                sol.pop()
            
            if open_count > close_count:
                sol.append(')')
                backtrack(open_count, close_count + 1)
                sol.pop()

        backtrack()
        return result


        


        