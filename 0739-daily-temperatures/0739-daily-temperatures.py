class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        ans = [0]* (len(temperatures))
        stack = []

        for idx, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                stack_t, stack_i = stack.pop()
                ans[stack_i] = idx - stack_i
            stack.append((t, idx))

        return ans



