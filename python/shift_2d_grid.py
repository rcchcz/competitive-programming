# https://leetcode.com/problems/shift-2d-grid/
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        r, c = len(grid), len(grid[0])
        N = r*c
        ans = [[0] * c for _ in range(r)]

        for i in range(N):
            j = (i + k) % N
            ans[j//c][j%c] = grid[i//c][i%c]
        
        return ans