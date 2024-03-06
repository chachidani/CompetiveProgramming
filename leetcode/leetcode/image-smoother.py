class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        if len(img[0]) ==1 and len(img) == 1:
            return img
        
        
        

        new_col = []
        new_row = []
        new_img = 0
        
        for row in range(len(img)):
            for col in range(len(img[0])):

                if row == 0 and row == len(img)-1 and col == 0:
                    summ = img[row][col] + img[row][col+1]
                    new_img = summ//2
                elif row == 0 and row == len(img)-1 and col == len(img[0])-1:
                    summ = img[row][col] + img[row][col-1]
                    new_img = summ//2
                elif col == 0 and col == len(img[0])-1 and row == 0:
                    
                    summ = img[row][col] + img[row+1][col]
                    new_img = summ//2
                elif col == 0 and col == len(img[0])-1 and row == len(img)-1:

                    summ = img[row][col] + img[row-1][col]
                    new_img = summ//2

                elif col == 0 and col == len(img[0])-1:
                    summ = img[row][col] + img[row+1][col] + img[row-1][col]
                    new_img = summ//3

                
                elif row == 0 and row == len(img)-1:
                    summ = img[row][col] + img[row][col+1] + img[row][col-1]
                    new_img = summ//3
                

                elif  row ==  0 and  col == 0 :
                    summ = img[row][col] + img[row][col+1] + img[row+1][col+1] + img[row+1][col]
                    new_img = summ//4
                   
                
                elif  row == 0 and col == len(img[0])-1:
                    summ = img[row][col] + img[row][col-1] + img[row+1][col-1] + img[row+1][col]
                    new_img = summ//4
                   
               
                elif  row == len(img)-1 and col == 0 :
                    summ = img[row][col]  + img[row][col+1]+img[row-1][col+1]+img[row-1][col]
                    new_img = summ//4
                    
                
                elif row == len(img)-1 and col == len(img[0])-1:
                    summ = img[row][col]+ img[row - 1][col - 1] + img[row][col - 1] + img[row-1][col]
                    new_img = summ//4
                    

                elif  row == 0:
                    summ =  img[row][col]+img[row][col+1]+img[row+1][col+1]+img[row+1][col]+img[row+1][col-1]+img[row][col-1]
                    new_img = summ//6
                    

                elif  col == 0:
                    summ = img[row][col] +   img[row + 1][col] + img[row+1][col+1] + img[row][col+1]+img[row-1][col+1]+img[row-1][col]
                    new_img = summ//6
                    

                elif row ==  len(img)-1:
                    summ = img[row][col]+ img[row - 1][col - 1] + img[row][col - 1]  + img[row][col+1]+img[row-1][col+1]+img[row-1][col]
                    new_img = summ//6
                    


                elif  col ==  len(img[0])-1:
                    summ = img[row][col]+ img[row - 1][col - 1] + img[row][col - 1] + img[row + 1][col - 1] + img[row + 1][col]   +img[row-1][col]
                    new_img = summ//6
                    

                else:
                    summ = img[row][col]+ img[row - 1][col - 1] + img[row][col - 1] + img[row + 1][col - 1] + img[row + 1][col] + img[row+1][col+1] + img[row][col+1]+img[row-1][col+1]+img[row-1][col]
                    new_img = summ//9
                new_col.append(new_img) 
            new_row.append(new_col)
            new_col = []
                
                   
        
        return new_row

             
        