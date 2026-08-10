class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []

        for s in strs:
            encoded.append(str(len(s)))
            encoded.append("#")
            encoded.append(s)
        return "".join(encoded)

        # should produce -> 5#Hello5#World
        # edge case "#" -> 1##
    def decode(self, s: str) -> List[str]:
        marker = 0
        i = 0
        decoded = []

        while i < len(s):
            x = s[i]
            if x != "#":
                i += 1
                continue 
            else: 
                string_length = int(s[marker:i])
                decoded.append(s[i + 1:i + string_length + 1])
                marker = i + string_length + 1
                i = marker
            
        return decoded