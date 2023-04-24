# https://leetcode.com/problems/last-stone-weight/
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # working with negative values so we can use a min heap
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first: heapq.heappush(stones, first-second)

        # append 0 in case stones is empty
        stones.append(0)
        return abs(stones[0])
        

        '''
        stones.sort()
        n = len(stones)-1
        
        while n > 0:
            x = stones.pop()
            y = stones.pop()
            
            if x == y: 
                n -= 2
            else: 
                stones.append(abs(y-x))
                stones.sort()
                n -= 1
            
        return stones[0] if stones else 0
        '''