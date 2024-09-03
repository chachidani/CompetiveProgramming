# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        count = defaultdict(list)
        for i in range(len(list1)):
            count[list1[i]].append(i)
        for i in range(len(list2)):
            count[list2[i]].append(i)
      
        minn = float('inf')
        for key,value in count.items():
            if len(value) == 2:
                minn = min(minn , sum(value))
       

        ans = []
        for key,value in count.items():
            if len(value) == 2:
                if sum(value) == minn:
                    ans.append(key)
        return ans
        