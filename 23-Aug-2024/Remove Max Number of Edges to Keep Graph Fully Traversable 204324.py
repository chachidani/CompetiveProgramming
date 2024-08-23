# Problem: Remove Max Number of Edges to Keep Graph Fully Traversable - https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1]*n
        self.count = n
     
    def find(self, x):
      
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
        
    
    def union(self, x, y):
        parent_x  = self.find(x)
        parent_y = self.find(y)

        if parent_x != parent_y:
            if self.rank[parent_x] > self.rank[parent_y]:
                self.parent[parent_y] = parent_x
            elif self.rank[parent_x] < self.rank[parent_y]:
                self.parent[parent_x] = parent_y
            else:
                self.parent[parent_y] = parent_x
                self.rank[parent_y] += 1
            self.count -= 1
            return 1
        return 0
            
    def isConnected(self):
        return self.count 

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edges.sort(reverse=True)
        unfA = UnionFind(n)
        unfB =  UnionFind(n)
        count = 0
    
        A = [1]*n
        B = [1]*n
        for t, x,y in edges:
            x -= 1
            y -= 1
           
            if t == 1:
                if unfA.union(x,y):
                    count += 1
                
                
            elif t == 2:
                if  unfB.union(x,y):
                    count += 1
                
             
            else:
                if unfA.union(x,y) | unfB.union(x,y):
                    count += 1
        
        
        if unfA.isConnected() > 1 or unfB.isConnected() > 1:
            return -1
        return len(edges) -  count

        