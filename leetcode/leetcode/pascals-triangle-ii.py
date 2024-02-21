class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        if rowIndex == 0:
            return  [1]
        per = self.getRow(rowIndex-1)
        row = [1]
        for i in range(1,len(per)):
            row.append(per[i-1] +per[i] )
        row.append(1)
        return row



    




        


            

        

            

        