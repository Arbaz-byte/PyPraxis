class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        prev, curr = 0,0

        for i in range(2, n+1):
            prev, curr = curr, min(cost[i-1]+curr, cost[i-2]+prev)
        return curr