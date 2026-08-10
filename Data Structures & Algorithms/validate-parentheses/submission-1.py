class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        opening = ['(', '{', '[']
        closing = [')', '}', ']']

        for c in s: 
            if c in opening:
                stack.append(c)

            if c in closing: 
                if len(stack) == 0: 
                    return False
                
                opener = stack.pop()

                if opening.index(opener) != closing.index(c):
                    return False
        if len(stack) == 0:
            return True
        else: 
            return False
            




        