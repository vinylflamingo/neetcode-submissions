class Solution:
    def maxScore(self, s: str) -> int:

        # brute 
        # split at every index, 
        # calculate left by count of 0s 
        # calculate right by count of 1s 
        # add together 
        # compare against current_max 
        # return final current_max 

        current_max = 0 
        list_s = list(s)
        for i in range(len(list_s)):
            left = list_s[:i]
            right = list_s[i:]

            left_sum = 0 
            right_sum = 0 

            if len(left) == 0 or len(right) == 0:
                continue

            for num in left: 
                if int(num) == 0: 
                    left_sum += 1
        
            for num in right: 
                if int(num) == 1: 
                    right_sum += 1
            

            total = left_sum + right_sum

            current_max = max(current_max, total)

        return current_max 


