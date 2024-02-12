# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        cur = ListNode(0,head)
        while cur.next:
            cur = cur.next
            arr.append(cur.val)
        
        reve_arr = arr[::-1]
        
        if arr == reve_arr:
            
            return True
        
        return False
    
        