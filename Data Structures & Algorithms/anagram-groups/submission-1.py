class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = defaultdict(list)
        base_ascii = ord("a")

        for n in strs:
            count = [0] * 26
            for j in n:
                index = ord(j) - base_ascii
                count[index] += 1

            key = tuple(count)

            result[key].append(n)
    
        return list(result.values())
        

            



            



            



        











        