class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        s_list = list(s)
        s_list.sort()
        stack = []

        is_odd = None
        if len(s) % 2 != 0:
            is_odd = True
        else: 
            is_odd = False 


        for char in s_list: 
            if len(stack) == 0:
                stack.append(char)
            elif len(stack) > 0: 
                if char == stack[-1]:
                    stack.pop()
                else: 
                    stack.append(char)
            
        
        if len(stack) > 1: 
            return False 
        elif len(stack) == 1:
            if is_odd: 
                return True
            else:
                return False
        return True
        