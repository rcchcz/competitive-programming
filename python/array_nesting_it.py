# https://leetcode.com/problems/array-nesting/
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        seen = set()
        output = 0

        for i in range(len(nums)):
            tmp = 0
            while i not in seen:
                seen.add(i)
                i = nums[i]
                tmp += 1
            
            output = max(tmp, output)
        
        return output