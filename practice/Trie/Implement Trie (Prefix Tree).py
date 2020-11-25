class TrieNode:
    def __init__(self):
        self.l = [None] * 26
        self.is_end = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tmp = self.head
        for i in word:
            if not tmp.l[ord(i) - ord('a')]:
                tmp.l[ord(i) - ord('a')] = TrieNode()
            tmp = tmp.l[ord(i) - ord('a')]
        
        tmp.is_end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tmp = self.head
        for i in word:
            if tmp.l[ord(i) - ord('a')]:
                tmp = tmp.l[ord(i) - ord('a')]
            else:
                return False
            
        return tmp.is_end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tmp = self.head
        for i in prefix:
            if tmp.l[ord(i) - ord('a')]:
                tmp = tmp.l[ord(i) - ord('a')]
            else:
                return False
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
