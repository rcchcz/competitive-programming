# https://leetcode.com/problems/simplify-path/
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for c in path.split("/"):
            if c == "" or c == ".": continue
            elif c == "..":
                if len(stack) > 0: stack.pop()
            else: stack.append(c)
        
        return "/"+"/".join(stack)