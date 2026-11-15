class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        pos_diag = set() # (r+c)
        neg_diag = set() # (r-c)

        def backtrack(r:int) -> int:

            # Base Case : All Queens are places
            if r == n:
                return 1
            
            count = 0 # Recode for correct arrengment
            for c in range(n):
                # Avoid restricted paths 
                if c in cols or r+c in pos_diag or r-c in neg_diag:
                    continue
                
                # Add the Qeen and block the paths 
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)

                # search new row
                count += backtrack(r+1)

                # backtrack : remove queen and clear the path 
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
            return count

        return backtrack(0)


                
        
                

        
        