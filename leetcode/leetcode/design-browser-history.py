class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = Node(homepage)
        self.cur = Node(homepage)
        

    def visit(self, url: str) -> None:
        newNode = Node(url)
        self.cur.next = newNode
        newNode.prev = self.cur
        self.cur = newNode
        

    def back(self, steps: int) -> str:
        while self.cur.prev and steps > 0:
            self.cur = self.cur.prev
            steps -=1
        return self.cur.val

    def forward(self, steps: int) -> str:
        while self.cur.next and steps > 0:
            self.cur = self.cur.next
            steps -=1
        return self.cur.val

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)