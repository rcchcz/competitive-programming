# https://leetcode.com/problems/maximum-number-of-balloons/
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # b a l o n (letters)
        # 1 1 2 2 1 (qnt)
        c = Counter(text)
        ans = float("inf")

        for l in "balon":
            if l in "ban": ans = min(ans, c[l])
            else: ans = min(ans, c[l]//2)
        
        return ans