# https://leetcode.com/problems/shifting-letters/
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        # [3,5,9] becomes [17,14,9] (cumulative shift)
        s = list(s)
        shifts = reversed(list(accumulate(list(reversed(shifts)))))

        for i,sh in enumerate(shifts):
            s[i] = chr((((ord(s[i]) - ord('a')) + sh) % 26) + 97)
        
        return "".join(s)