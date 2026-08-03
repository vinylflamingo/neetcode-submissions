class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        j = 0 

        for i in range(len(operations)):
            print("i = " + str(i) + ", j = " + str(j) + ", current record = " + str(record))
            if operations[i] == "D":
                record.append(record[j - 1] * 2)
                j += 1
            elif operations[i] == "C":
                record.pop()
                j -= 1
            elif operations[i] == "+":
                record.append(record[j - 1] + record[j - 2])
                j += 1
            else: 
                record.append(int(operations[i]))
                j += 1                    
        return sum(record)

                 


        
        



                    

                    
                
        