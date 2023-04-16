# https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        mod = 10**9 + 7

        cnt = defaultdict(int) # (index, char) -> count among all words
        for w in words:
            for i, c in enumerate(w): cnt[(i, c)] += 1

        dp = {} # (i, k) -> num of ways
        # i = index of target, k = index of words[j][k]
        def dfs(i, k):
            if i == len(target): return 1 # target builded
            if k == len(words[0]): return 0 # no more chars; target not builded
            if (i, k) in dp: return dp[(i, k)] # cached value

            c = target[i]
            dp[(i, k)] = dfs(i, k+1) # skip k position
            dp[(i, k)] += cnt[(k, c)] * dfs(i+1, k+1)

            return dp[(i, k)] % mod
        
        return dfs(0, 0)