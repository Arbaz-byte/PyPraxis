class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:

        # Track of columns, and diagonals
        cols = set()
        post_diag = set()  # r+c
        neg_diag = set()   # r-c

        result = []
        board = [["."]*n for _ in range(n)] # nxn board

        def backtrack(r: int):

            # Base Case : when placed all Queens 
            if r == n:
                copy = ["".join(row) for row in board]
                result.append(copy)
                return
            
            for c in range(n):

                # Check valid attack positions 
                if c in cols or r+c in post_diag or r-c in neg_diag:
                    continue

                # Place Queen and recode the Attack
                cols.add(c)
                post_diag.add(r+c)
                neg_diag.add(r-c)
                board[r][c] = "Q"

                # Move to next row
                backtrack(r + 1)

                # Backtrack : remove queen and attack
                cols.remove(c)
                post_diag.remove(r+c)
                neg_diag.remove(r-c)
                board[r][c] = "."
            
        backtrack(0)
        return result
            





        