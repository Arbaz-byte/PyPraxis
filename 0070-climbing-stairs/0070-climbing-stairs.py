class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        prev, curr = 1, 2
        for i in range(n-2):
            curr, prev = curr + prev, curr
        
        return curr