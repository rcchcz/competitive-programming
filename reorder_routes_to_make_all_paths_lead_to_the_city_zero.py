# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description/
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # start at node 0
        # recursively check its neighbors (dfs)
        # count changes (no need to really do the change)        
        edges = { (a,b) for a,b in connections }
        neighbors = {city:[] for city in range(n) }
        visited = set()
        changes = 0

        for a,b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)

        def dfs(city):
            nonlocal edges, neighbors, visited, changes
            for neighbor in neighbors[city]:
                if neighbor in visited:
                    continue
                # check if this neighbor can reach city 0
                if (neighbor, city) not in edges:
                    changes += 1
                visited.add(neighbor)
                dfs(neighbor)
        
        visited.add(0)
        dfs(0)

        return changes