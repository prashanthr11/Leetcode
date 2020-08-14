from itertools import combinations as cmb

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.combinationLength = combinationLength
        self.l = list(cmb(characters, combinationLength))
        

    def next(self) -> str:
        ret = ""
        for i in self.l[0]:
            ret += i
        self.l.pop(0)
        return ret

    def hasNext(self) -> bool:
        return len(self.l)
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
