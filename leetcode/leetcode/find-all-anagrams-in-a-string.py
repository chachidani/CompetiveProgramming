class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
      target, shash = {},{}
      if len(p)>len(s):
        return []

      for i in range(len(p)):
        target[p[i]] = 1 + target.get(p[i],0)
        shash[s[i]] = 1 + shash.get(s[i],0)
      res = [0] if target == shash else []
      l = 0
      for r in range(len(p),len(s)):
        shash[s[r]] = 1 + shash.get(s[r],0)
        shash[s[l]] -= 1
        if shash[s[l]] == 0:
          shash.pop(s[l])
        l+=1
        if target == shash:
          res.append(l)
        
      return res

          




        