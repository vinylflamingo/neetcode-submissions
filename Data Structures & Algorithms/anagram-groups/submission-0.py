class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = {}

        for i, n in enumerate(strs):
            count = [0] * 26

            for j in n:
                index = ord(j) - ord("a")
                count[index] += 1

            key = tuple(count)

            if key not in result:
                result[key] = []

            result[key].append(n)
        
        answer = []
        for value in result: 
            answer.append(result[value])
        return answer
        

            



            



            



        











        