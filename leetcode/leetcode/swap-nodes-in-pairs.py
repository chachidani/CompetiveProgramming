# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(0,head)

        prev,cur =dummy, head
        
        while cur and cur.next:
            temp = cur.next
            temp2 = cur.next.next
            temp.next = cur
            cur.next = temp2
            prev.next = temp
            prev = cur
            cur = temp2
        return dummy.next
        
        
        