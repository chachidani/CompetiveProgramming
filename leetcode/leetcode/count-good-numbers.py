class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def myPow( x,b):
            if b==0:
                return 1
            if b==1:
                return x
        
            
            if b%2 ==0:
                return (myPow(x,b//2) **2)%(10**9 + 7)
            else:
                return ((myPow(x,b//2) **2) * x)%(10**9 + 7)
        q = n//2
        if n % 2 == 0:
            return (myPow(5,q) * myPow(4,q))%(10**9 + 7)
        else:
            return (myPow(5,q) * myPow(4,q)*5)%(10**9 + 7)
        
       
        