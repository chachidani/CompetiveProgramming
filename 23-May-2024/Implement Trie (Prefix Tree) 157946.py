# Problem: Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode:
    def __init__(self):
        
        self.children  = [None for i in  range(26)]
        self.end = False
    
class Trie:

    def __init__(self):
        self.root = TrieNode()
       


        

    def insert(self, word: str) -> None:
        node = self.root

        for cr in word:
            idx = ord(cr) - ord('a')
            if not node.children[idx]:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.end = True

        

    def search(self, word: str) -> bool:
        node = self.root

        for cr in word:
            idx = ord(cr) - ord('a')
            if not node.children[idx]:
                return False
            node = node.children[idx]
        return node.end
        

        

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for cr in prefix:
            idx = ord(cr) - ord('a')
            if not node.children[idx]:
                return False
            node = node.children[idx]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
