class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:

        hash_map = {ch: i for i, ch in enumerate(keyboard)}

        count = 0
        last_seen = 0
        for w in word: 
            i = hash_map[w]
            count += abs(i - last_seen)
            last_seen = i
        
        return count





