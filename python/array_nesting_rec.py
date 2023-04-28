# https://leetcode.com/problems/array-nesting/
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        seen = set()
        @lru_cache()

        def rec(st):
            if st not in seen:
                seen.add(st)
                return 1+rec(nums[st])
            else:
                return 0
        
        return max([rec(i) for i in range(len(nums))])