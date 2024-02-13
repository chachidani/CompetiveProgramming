# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        if not head or not head.next:
            return head
        
        odd  = cur = head
        even = cur2 = point = head.next

        
        while even and even.next:
            odd = odd.next.next
            cur.next = odd
            cur = odd
            even = even.next.next
            cur2.next = even
            cur2 = even

        cur.next = point
        

            
        return dummy.next


       

         


        