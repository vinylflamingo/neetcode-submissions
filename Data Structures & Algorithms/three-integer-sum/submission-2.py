class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
    
        for i in range(0 , len(nums) -2, 1):
            j, k = i + 1, len(nums) - 1
        
            while j < k: 
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    if [nums[i], nums[j], nums[k]] not in result:
                        result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
            
        return result
