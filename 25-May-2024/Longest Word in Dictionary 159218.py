# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}
        
class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:  
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            
            curr = curr.children[char]
        curr.is_end = True

    def chack(self, word: str) -> bool:
        curr = self.root.children[word[0]]
        for ch in word[1:]:
            if not curr.is_end:
                return False
            curr = curr.children[ch]
        return True
        

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key = lambda x: (-len(x), x))
        trie = Trie()
        for word in words:
            trie.insert(word)
     
        for word in words:
            if trie.chack(word):
                return word
        return ''




































        