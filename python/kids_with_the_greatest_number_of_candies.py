# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        ans = []

        for k in candies:
            ans.append(k + extraCandies >= m)
        
        return ans