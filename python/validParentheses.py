class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        stack = []

        for i in range(n):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            elif s[i] == ')':
                if len(stack) == 0 or stack[-1] != '(':
                    return False
                stack.pop()
            elif s[i] == '}':
                if len(stack) == 0 or stack[-1] != '{':
                    return False
                stack.pop()
            elif s[i] == ']':
                if len(stack) == 0 or stack[-1] != '[':
                    return False
                stack.pop()

        return False if len(stack) else True
                
link = 'https://leetcode.com/problems/valid-parentheses/?envType=study-plan-v2&envId=top-interview-150'