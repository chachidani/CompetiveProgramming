# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head


        cur = head
        while cur and cur.next:
            if type(cur.next.val) == str:
                cur.next.val = str(cur.val)
                return cur.next
            if cur.next == None:
                return -1
            cur.val = str(cur.val)
            cur = cur.next
        

            

        
            

        
