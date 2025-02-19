class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for item in path.split("/"):
            if stack and item == "..":
                stack.pop()
            elif item == "." or item == ".." or item == "":
                pass
            else:
                stack.append(item)
                
        return "/" + "/".join(stack)

link = 'https://leetcode.com/problems/simplify-path/description/?envType=study-plan-v2&envId=top-interview-150'