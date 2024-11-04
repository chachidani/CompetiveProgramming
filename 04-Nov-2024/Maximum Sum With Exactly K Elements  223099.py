# Problem: Maximum Sum With Exactly K Elements  - https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/description/

from queue import PriorityQueue
class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        pq=PriorityQueue()
        sm=0
        for num in nums:
            pq.put(-1*num)
        while k>0:
            val=-1*pq.get()
            sm+=val
            pq.put(-1*(val+1))
            k-=1
        return sm