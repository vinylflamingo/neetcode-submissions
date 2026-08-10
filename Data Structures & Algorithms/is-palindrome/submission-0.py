class Solution:
    def isPalindrome(self, s: str) -> bool:

        i, j = 0, len(s) - 1

        valid_chars = [
            "a", "b", "c", "d", "e", "f", "g", 
            "h", "i", "j", "k", "l", "m", "n", 
            "o", "p", "q", "r", "s", "t", "u", 
            "v", "w", "x", "y", "z", "0", "1",
            "2", "3", "4", "5", "6", "7", "8",
            "9"
            ]

        while i < j:
            if s[i].lower() not in valid_chars:
                i += 1
                continue
            
            if s[j].lower() not in valid_chars:
                j -= 1
                continue
            
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
                continue
            else: 
                return False
        
        return True


                    