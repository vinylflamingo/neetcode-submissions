class Solution:
    def maxScore(self, s: str) -> int:
        
        # O(n) solution 
        # instead of splitting at every index 
        # and recalculating, we keep a running 
        # tally of left and right. Then we 
        # simply check the current index and 
        # adjust the running tallys. 

        
        # we instantiate this as if the left 
        # slice is empty, and the right slice
        # is the whole array. but we do NOT consider this 
        # as one of the results. 
        zeros = 0 
        ones = s.count("1")
        result = 0 

        # in this solution, we apply -1 to the len 
        # because we wont be calculating the final
        # index, as that would result in a empty right 
        # set. 
        for i in range(len(s) - 1):

            # We check the index to see if its a 0 or 1
            if s[i] == "0":
                # if its a 0, that means were adding a 0 
                # to the LEFT slice. In the left slice, 0s
                # are counted up
                zeros += 1
            else: 
                # otherwise if its one, were removing it 
                # from the RIGHT slice which counts 1's up. 
                # meaning were losing one of the count. 
                ones -= 1

            result = max(result, zeros + ones)

        return result