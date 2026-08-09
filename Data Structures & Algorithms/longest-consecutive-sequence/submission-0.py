class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        set_nums = set(nums)
        highest_count = 0

        for n in set_nums: 
            count = 1
            if n - 1 not in set_nums: 
                x = n
                while True: 
                    if x + 1 in set_nums: 
                        count += 1 
                        x += 1
                    else: 
                        break
            if count > highest_count: 
                highest_count = count
        
        return highest_count
            

        
                

                

        