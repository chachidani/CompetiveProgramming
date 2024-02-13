# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(0,head)
        prev = dummy
        leftB = head
        
        new = None
        for _ in range(left-1):
            prev = leftB
            leftB = leftB.next
        for _ in range(right-left + 1):        
            temp = leftB.next
            leftB.next = new
            new = leftB
            leftB = temp
     
        prev.next.next= leftB
        prev.next = new

        
        return dummy.next



        




        




        
            