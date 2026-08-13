class Solution:
    def confusingNumber(self, n: int) -> bool:

        digit_list = [int(x) for x in str(n)]

        if set([2,3,4,5,7]) & set(digit_list):
            return False 
        
        rotated_digits = []
        for digit in digit_list:
            if digit == 6: 
                rotated_digits.append("9")
            elif digit == 9:
                rotated_digits.append("6")
            else:
                rotated_digits.append(str(digit))

        new_number = int("".join(rotated_digits[::-1]))

        
        return new_number != n
