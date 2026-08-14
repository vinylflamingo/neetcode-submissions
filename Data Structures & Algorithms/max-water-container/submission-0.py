class Solution:
    def maxArea(self, heights: List[int]) -> int:

        i, j = 0, len(heights) - 1
        max_i = heights[i] 
        max_j = heights[j]

        max_total = (j - i) * min(max_j, max_i)

        while i < j: 
            if heights[i] < heights[j]:
                i += 1
                if max_i < heights[i]:
                    max_i = heights[i]
                    max_total = max(max_total, (j - i) * min(max_j, max_i))
                else: 
                    continue
            else: 
                j -= 1
                if max_j < heights[j]:
                    max_j = heights[j]
                    max_total = max(max_total, (j - i) * min(max_j, max_i))
                else:
                    continue 
        
        return max_total




        