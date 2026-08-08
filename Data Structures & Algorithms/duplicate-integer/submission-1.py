class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        store = {}

        for i, n in enumerate(nums):
            if n in store: 
                return True
            else: 
                store[n] = i
        
        return False



 