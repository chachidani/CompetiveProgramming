# Problem: Vowel of All Substring - https://leetcode.com/problems/vowels-of-all-substrings/

class Solution:
    def countVowels(self, word: str) -> int:
        vowels = ['a' , 'e' , 'i' , 'o' , 'u']
        
        
        ans = 0
        for i in range(len(word)):
            
            if word[i] in vowels:
                x = i
                y = (len(word)-1 - i) 
                ans += x + x*y+1 + y
            
 
        return ans
        
        