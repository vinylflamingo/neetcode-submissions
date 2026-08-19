class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        i, k = 0, 0
        largest = 0 
        window = set()

        while k < len(s):
            if s[k] not in window:
                window.add(s[k])
                k += 1
                largest = max(largest, len(window))
            elif s[k] in window:
                window.remove(s[i])
                i += 1

        return largest
        