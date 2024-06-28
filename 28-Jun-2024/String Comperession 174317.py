# Problem: String Comperession - https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
       
        write_idx = 0
        i = 0
        
        
        while i < len(chars):
            
            j = i + 1
            while j < len(chars) and chars[j] == chars[i]:
                j += 1

            
            chars[write_idx] = chars[i]
            write_idx += 1
            if j - i > 1:
                count_str = str(j - i)
                chars[write_idx:write_idx+len(count_str)] = count_str
                write_idx += len(count_str)

            
            i = j

       
        del chars[write_idx:]

        
        return len(chars)