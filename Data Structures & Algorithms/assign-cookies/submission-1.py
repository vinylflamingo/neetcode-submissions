class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        

        # brute force solution 
        g.sort()
        s.sort()

        i, j = 0, 0 

        satisfied = 0

        while j < len(s) and i < len(g):
            if g[i] <= s[j]: 
                satisfied += 1
                i += 1
                j += 1
            else: 
                j += 1

        return satisfied

    

        