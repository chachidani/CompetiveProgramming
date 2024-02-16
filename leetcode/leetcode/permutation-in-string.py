class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        l, r = 0, 0
        t = dict()
        win = dict()

        for i in range(len(s1)):
            t[s1[i]] = t.get(s1[i], 0) + 1

        while r < len(s2):
            win[s2[r]] = win.get(s2[r], 0) + 1
            if r - l + 1 == len(s1):
                if sorted(win.items()) == sorted(t.items()):
                    return True
                else:
                    win[s2[l]] -= 1
                    if win[s2[l]] == 0:
                        del win[s2[l]]
                    l += 1
            r += 1

        return False
