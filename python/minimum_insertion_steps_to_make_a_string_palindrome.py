# https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        INF = 10 ** 20

        has_cache = [[False] * n for _ in range(n)]
        cache = [[None] * n for _ in range(n)]

        # inclusive bounds
        def getMin(left, right):
            if left >= right: return 0
            if has_cache[left][right]: return cache[left][right]
            
            best = INF
            
            if s[left] == s[right]: best = min(best, getMin(left+1, right-1))

            best = min(best, getMin(left+1, right) + 1)
            best = min(best, getMin(left, right-1) + 1)

            has_cache[left][right] = True
            cache[left][right] = best
            return best
        
        return getMin(0, n-1)