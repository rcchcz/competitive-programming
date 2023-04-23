# https://leetcode.com/problems/restore-the-array/
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        MOD = 10**9 + 7
        N = len(s)
        has_cache = [False] * (N + 1)
        cache = [0] * (N + 1)

        # index -> 0 to N
        def count(index):
            if index == N: return 1
            if s[index] == "0": return 0
            if has_cache[index]: return cache[index]

            total = 0
            curr = 0
            curr_index = index

            while curr_index < N and curr <= k:
                curr *= 10
                curr += int(s[curr_index])

                if curr <= k:
                    total += count(curr_index + 1)
                    total %= MOD
                
                curr_index += 1
            
            has_cache[index] = True
            cache[index] = total % MOD
            return cache[index]

        return count(0)     