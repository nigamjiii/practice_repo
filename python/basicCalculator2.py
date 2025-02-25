class Solution:
    def calculate(self, s: str) -> int:
        i = 0
        op = "+"
        stack = []

        while i < len(s):
            if s[i].isdigit():
                t = 0
                while i < len(s) and s[i].isdigit():
                    t = (t * 10) + int(s[i])
                    i += 1

                if op == "+":
                    stack.append(t)
                elif op == "-":
                    stack.append(-t)
                elif op == "*":
                    temp = stack.pop()
                    stack.append(temp * t)
                elif op == "/":
                    temp = stack.pop()
                    stack.append(int(temp / t))
                continue
            elif s[i] != " ":
                op = s[i]

            i += 1

        return sum(stack)

link = 'https://leetcode.com/problems/basic-calculator-ii/'