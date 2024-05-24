# Problem: Search Suggestions System - https://leetcode.com/problems/search-suggestions-system/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}
class Trie:

    def __init__(self):
        self.root = TrieNode()
        self.store = defaultdict(list)

    def insert(self, word: str) -> None:  
        curr = self.root
        my_store = self.store
        l = ''
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            l += char
            my_store[l].append(word)
            curr = curr.children[char]
        curr.is_end = True
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        tire = Trie()
        for word in products:
            tire.insert(word)
        
        l = ''
        ans = []
        for word in searchWord:
            l += word
            tire.store[l].sort()
            ans.append(tire.store[l][:3])
        return ans













        