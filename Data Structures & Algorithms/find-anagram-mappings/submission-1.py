class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        

        nums2_map = {}

        for i, num in enumerate(nums2):
            if num in nums2_map:
                nums2_map[num].append(i)
            else:
                nums2_map[num] = [i]

        output = []
        for num in nums1:
            value = nums2_map[num].pop()
            output.append(value)
        
        return output


        