# https://leetcode.com/problems/island-perimeter/
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= R or c < 0 or c >= C or grid[r][c] == 0:
                return 1
            
            if grid[r][c] == 1:
                grid[r][c] = 2 # mark as visited
                return dfs(r-1, c) + dfs(r+1, c) + dfs(r, c-1) + dfs(r, c+1)
            
            return 0
        
        perimeter = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    perimeter += dfs(r, c)

        return perimeter