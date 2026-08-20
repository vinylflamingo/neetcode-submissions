class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        

        nums2_map = {}

        for i, num in enumerate(nums2):
            nums2_map[num] = i

        output = []
        for num in nums1:
            output.append(nums2_map[num])
        
        return output


        