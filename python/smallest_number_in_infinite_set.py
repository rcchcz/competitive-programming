# https://leetcode.com/problems/smallest-number-in-infinite-set/
from sortedcontainers import SortedSet
class SmallestInfiniteSet:

    def __init__(self):
        self.sl = SortedSet()
        for i in range(1, 1005): self.sl.add(i)
        
    def popSmallest(self) -> int:
        n = self.sl[0]
        self.sl.remove(n)
        return n        

    def addBack(self, num: int) -> None:
        self.sl.add(num)        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)