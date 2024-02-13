# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        cur = head
        
        while cur:
            myval = head
            while myval != cur :
                if myval.val > cur.val:
                    myval.val, cur.val = cur.val ,  myval.val
                

                myval = myval.next
            cur = cur.next
        return head


                    


