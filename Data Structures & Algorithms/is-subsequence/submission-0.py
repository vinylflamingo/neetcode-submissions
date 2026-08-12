class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_stack = list(s[::-1])

        for x in t: 
            if not s_stack: 
                return True
            if s_stack[-1] == x: 
                s_stack.pop()

        if not s_stack: 
            return True
        return False
            









        