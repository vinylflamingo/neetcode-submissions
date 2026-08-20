class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:

        distinctSet = set()
        for n in nums: 
            if n not in distinctSet:
                distinctSet.add(n)
            else: 
                distinctSet.remove(n)
        return max(distinctSet) if distinctSet else -1
        