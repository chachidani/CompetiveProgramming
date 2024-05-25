# Problem: Replace Words - https://leetcode.com/problems/replace-words/

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
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        store = list(map(str, sentence.split()))
        tria = Trie()
        for word in store:
            tria.insert(word)
    
        
        ans = ''
        for word in store:
            curr = tria.root
            let = ''
            
            for ch in word:
                let += ch
                
                if let in dictionary:
                    break
                curr = curr.children[ch]
          
            ans += let + ' '
            
        return ans[:len(ans)-1]
                














