# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        less = ListNode(-1,None)
        dummy = less
        great =  ListNode(-1,None)
        cur_great =  great
         
        cur  = head
        while  cur:
            if cur.val < x:
                less.next = cur
                less = cur
                cur = cur.next
                less.next = None
                print("less" , less.val)

            else:
                great.next = cur
                great = cur
                cur = cur.next
                great.next = None
                
                print("great" , great.val)
        less.next = cur_great.next
        
        
        
        
        
        return dummy.next


        