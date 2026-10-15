class Solution:
    def isValid(self, s: str) -> bool:

        hasmap = {')' : '(', ']':'[', '}':'{'}
        stack = []
        for close in s:
            if close not in hasmap:
                stack.append(close)
            else:
                if not stack:
                    return False
                else:
                    popped = stack.pop()
                    if popped != hasmap[close]:
                        return False
        
        return not stack
        