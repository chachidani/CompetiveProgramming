# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:  
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end = True
        
   
        


    def search(self, word: str) -> bool:
        curr = self.root
        for x in range(len(word)):
            c = word[x]
            if c == ".":
                for j in range(26):
                    let = chr(97+j)
                    if let in curr.children:
                        comp = self.search(word[:x]+let+word[x+1:])
                        if comp:
                            return True
                return False
            
            if c not in  curr.children:
                return False
            curr = curr.children[c]
        return curr.is_end


           


        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)