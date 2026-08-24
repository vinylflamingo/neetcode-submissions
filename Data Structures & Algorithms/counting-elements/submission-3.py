class Solution:
    def countElements(self, arr: List[int]) -> int:

        num_set = set(arr)
        count = 0 
        
        for x in arr: 
            if x + 1 in num_set: 
                count += 1
        
        return count