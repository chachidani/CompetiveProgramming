# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if not head or not head.next:
            return head.val
        prev = None
        cur = head
        temp = cur.next
        
        while temp:
            cur.next = prev
            prev = cur
            cur = temp
            temp = temp.next
        cur.next = prev

        size = 0
        myval = 0
        while cur:
            myval += (2**size) * cur.val
            cur = cur.next
            size +=1
        return myval

        