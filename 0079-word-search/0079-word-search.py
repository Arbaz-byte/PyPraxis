class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        
        rows, cols = len(board), len(board[0])
        def dfs(r: int, c: int, index: int) -> bool:
            
            # Base case : Matches all char in the word
            if index == len(word):
                return True

            # Out of bound and char mismatch
            if r<0 or r >= rows or c<0 or c>= cols or board[r][c] != word[index]:
                return False

            # Tempory mask for visited 
            temp = board[r][c]
            board[r][c] = "#"

            # Explore all four adjacent paths 
            found = (
                dfs(r+1, c, index+1) or # bottom
                dfs(r-1, c, index+1) or # top
                dfs(r, c+1, index+1) or # right
                dfs(r, c-1, index+1) # left
            )

            # Backtrack : restore original char
            board[r][c] = temp
            return found

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and dfs(r,c, 0):
                    return True
        return False