# https://leetcode.com/problems/happy-number/
class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        # check loops
        while n not in visited:
            if n == 1: return True

            visited.add(n)
            n = self.sumOfSquares(n)

        return False

    def sumOfSquares(self, n: int) -> int:
        ans = 0

        while n:
            digit = n % 10
            digit **= 2
            ans += digit
            n //= 10
        
        return ans        