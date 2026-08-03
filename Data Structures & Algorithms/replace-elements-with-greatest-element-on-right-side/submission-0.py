class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        current_max = 0
        for i in range(len(arr) - 1, -1, -1):
            if i == len(arr) - 1: 
                current_max = arr[i]
                arr[i] = -1
            else: 
                ele = arr[i]
                arr[i] = current_max
                if ele > current_max: 
                    current_max = ele
                
        return arr