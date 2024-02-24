# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = []
        def addnum(l1):
            nonlocal ans
            if  l1:
                addnum(l1.next)
                if len(ans) == 0 :
                    ans.append((l1.val)*10)
                    
                else:
                    ans[-1] = (ans[-1] + l1.val)*10
            return ans
        x = addnum(l1)
        ans = []
        y = addnum(l2)
        
        r  = x[-1]//10
        l = y[-1]//10
        strr = str(r+l)
        answer = dummy = ListNode(1)

        for i in range(len(strr)-1 , -1 , -1):
            answer.next = ListNode(int(strr[i]))
            answer = answer.next
        return dummy.next
        
            
            


        