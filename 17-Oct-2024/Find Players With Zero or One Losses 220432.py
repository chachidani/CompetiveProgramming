# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner = defaultdict(int)
        loser = defaultdict(int)
        for w , l in matches:
            winner[w]   +=1
            loser[l]   +=1
        ans = [[] , []]
        for l , g in loser.items():
            if g == 1:
                ans[1].append(l)
        for w , g in winner.items():
            if w not in loser:
                ans[0].append(w)
        ans[0].sort()
        ans[1].sort()

        return ans


        
        
 


        
        