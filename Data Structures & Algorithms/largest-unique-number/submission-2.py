class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:

        nums_stack = []
        nums.sort()
        last_num = -1
        for num in nums:
            if num not in nums_stack: 
                nums_stack.append(num)
                last_num = num
            elif num in nums_stack:
                nums_stack.pop()
                last_num = num
            elif num == last_num:
                continue 
            
        if len(nums_stack) > 0: 
            return nums_stack[-1]
        else: 
            return -1
        
            

        