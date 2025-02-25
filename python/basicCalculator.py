class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        res = curr = 0
        sign = 1
        i = 0
        stack = []

        while i < n:
            if s[i].isdigit():

                while i < n and s[i].isdigit():
                    curr = (curr * 10) + int(s[i])
                    i += 1

                res += sign * curr
                sign = 1
                curr = 0
                continue
            elif s[i] == "+":
                sign = 1
            elif s[i] == "-":
                sign = -1
            elif s[i] == "(":
                stack.append(res)
                stack.append(sign)

                sign = 1
                res = 0
            elif s[i] == ")":
                prev_sign = stack.pop()
                prev_ans = stack.pop()
                res = prev_ans + (prev_sign * res)
                sign = 1

            i += 1

        return res

link = 'https://leetcode.com/problems/basic-calculator/?envType=study-plan-v2&envId=top-interview-150'