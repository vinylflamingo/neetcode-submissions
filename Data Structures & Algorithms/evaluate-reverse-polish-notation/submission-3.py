class Solution:
    def isNumber(self, s) -> bool:
        try: 
            int(s)
            return True
        except:
            return False 

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for x in tokens: 
            if self.isNumber(x):
                stack.append(int(x))
            else: 
                if x == "+":
                    y = stack.pop()
                    z = stack.pop()
                    value = z + y
                    stack.append(value)
                if x == "*":
                    y = stack.pop()
                    z = stack.pop()
                    value = z * y
                    stack.append(value)
                if x == "-":
                    y = stack.pop()
                    z = stack.pop()
                    value = z - y
                    stack.append(value)
                if x == "/":
                    y = stack.pop()
                    z = stack.pop()
                    value = z / y
                    
                    stack.append(int(value))
        return stack.pop()



        