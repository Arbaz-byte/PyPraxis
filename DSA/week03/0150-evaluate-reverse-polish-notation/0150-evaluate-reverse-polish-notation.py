class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }

        for t in tokens:
            if t in ops:
                stack[-2] = ops[t](int(stack[-2]), int(stack[-1]))
                stack.pop()
            else:
                stack.append(t)
        return int(stack[0])








        