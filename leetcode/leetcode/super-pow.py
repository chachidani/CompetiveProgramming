class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        def change(b):
            n = 0
            for e in b:
                n = n*10 +e
            return n
        
        
      
        def myPow(x,n):
            if x == 0:
                return 0
            if n==0:
                return 1
            if n==1:
                return x
            
            if n%2 ==0:
                return (myPow(x,n//2) **2)%1337
            else:
                return (myPow(x,n//2) **2) * x % 1337
        
        return myPow(a,change(b))
        
        
            
        
        
        
       
            
        
            

        


        
        