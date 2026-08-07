class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seenNumbers = {}

        for n in range(len(nums)): 
            i = target - nums[n]
            
            if i in seenNumbers:
                return [seenNumbers[i], n] 

            if nums[n] not in seenNumbers: 
                seenNumbers[nums[n]] = n

