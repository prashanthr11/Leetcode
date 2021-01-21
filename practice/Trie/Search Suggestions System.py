class Trie:
    def __init__(self):
        self.trie = [None] * 26
        self.isend = False


class Solution:
    
    # Time: O(N) Where N is the total characters in the given words.
    # Space: O(26 * M) --> O(M) Where M is the longest length of the word
    
    def getword(self, root, tmp):
        if len(self.ans) == 3:
            return
        
        if root.isend:
            self.ans.append(tmp)
        
        for i in range(26):
            if root.trie[i]:
                self.getword(root.trie[i], tmp + chr(i + 97))
        
    
    def add(self, root, i):
        tmp = root
        for char in i:
            if not tmp.trie[ord(char) - ord('a')]:
                tmp.trie[ord(char) - ord('a')] = Trie()
            tmp = tmp.trie[ord(char) - ord('a')]
        tmp.isend = True
                
    def search(self, root, i):
        tmp = ''
        for j in i:
            if root.trie[ord(j) - ord('a')]:
                root = root.trie[ord(j) - ord('a')]
                tmp += j
            else:
                self.ret.append([])
                return
            
        self.getword(root, tmp)
        self.ret.append(self.ans)
    
    def suggestedProducts(self, a, b):
        root = Trie()
        for i in a:
            self.add(root, i)
        
        self.ret = list()
        self.ans = list()
        
        for i in range(1, 1 + len(b)):
            self.search(root, b[:i])
            self.ans = list()
            
        return self.ret
