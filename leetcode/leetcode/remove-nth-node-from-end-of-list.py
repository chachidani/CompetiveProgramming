# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        if not head.next:
            head = None
            return head
            
        cur = head
        temp = head
        size = 1
        while temp.next:
            temp = temp.next
            size += 1
        if size == n:
            dummy.next = cur.next
        else:
    
            for i in range(1,size - n):
                cur = cur.next
            if cur.next.next:
                cur.next = cur.next.next
            else:
                cur.next = None
        return dummy.next


        

        
        



