# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        prev = None
        cur = head
        temp = cur.next
        
        while temp:
            cur.next = prev
            prev = cur
            cur = temp
            temp = temp.next
        cur.next = prev
        

        return cur

        
            
        