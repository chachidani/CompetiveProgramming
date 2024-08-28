# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
        
    
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
          
    def get(self, x, y):
        return self.parent[x] == self.parent[y]

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        for x,y in edges:
            x -= 1
            y -= 1
            
            if uf.find(x) == uf.find(y):
                return [x+1,y+1]
            uf.union(x,y)
            
        
        
        
        





        


        

        