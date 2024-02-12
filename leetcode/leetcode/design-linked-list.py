class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0
        
        

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        
        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur.val


        

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
         
        newNode.next = self.head
        self.head = newNode
        self.size += 1
        
        

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        if not self.head :
            self.head = newNode
            
        else:
            cur = self.head
            while  cur.next:
                cur = cur.next
            cur.next = newNode
        self.size += 1
    

        
 
    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        elif index == 0:
            self.addAtHead(val)
        else:
            newNode = Node(val)
            
            cur = self.head
            for i in range(index-1):
                cur = cur.next
            newNode.next = cur.next
            cur.next = newNode
            self.size += 1
            
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
        else:
            cur = self.head
            for i in range(index-1):
                cur = cur.next
            
            cur.next = cur.next.next
        self.size -= 1


        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)