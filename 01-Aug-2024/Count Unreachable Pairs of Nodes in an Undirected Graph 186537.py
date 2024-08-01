# Problem: Count Unreachable Pairs of Nodes in an Undirected Graph - https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

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
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        uff = UnionFind(n)
        for i in range(len(edges)):
            uff.union(edges[i][0],edges[i][1])
     
        for i in range(n): 
            uff.parent[i] = uff.find(i)

        count = Counter(uff.parent)
        
        lengths = count.values()
        
     
        answer = (n*(n-1))//2 
        for length in lengths: 
            answer -= (length*(length-1))//2 

        return answer
      

        

   
